import datetime
import time

from flask import Flask, request, stream_with_context, Response
from flask_restful import Api, Resource
from walrus import (Model, TextField, Database, DateField)

from config import config
from sse import REDIS_CONN, stream, publish


db = Database(host='localhost', port=6379)


class Issue(Model):
    __database__ = db
    issue_name = TextField(index=True)
    id = TextField(primary_key=True, default=lambda: str(
        time.time()).replace('.', ''))
    date_created = DateField(default=datetime.datetime.now, index=True)

    def serialize(self):
        return dict(id=self.id,
                    name=self.issue_name,
                    date_created=str(self.date_created))


class IssueResource(Resource):

    def get(self):
        all_issues = Issue.all()
        if all_issues:
            return dict(data=[issue.serialize() for issue in all_issues],
                        message="success retrival.")
        return dict(message="No issues to display.")

    def post(self):
        name = request.get_json().get('name')
        issue = Issue.create(issue_name=name)
        issue.save()
        publish("New issue created")
        return dict(data=issue.serialize(),
                    message="issue created successfully."), 201

    def put(self):
        name = request.get_json().get('name')
        new_name = request.get_json().get('new_name')
        expr = (Issue.issue_name == name)
        for issue in Issue.query(expr):
            print(issue)
            if issue:
                issue.issue_name = new_name
                issue.save()
                return dict(issue.serialize(),
                            message="Issue update successful"), 200
            return dict(message="Oops no issue with the name."), 404

    def delete(self):
        name = request.get_json().get('name')
        expr = (Issue.issue_name == name)
        for issue in Issue.query(expr):
            if issue:
                issue.delete()
                return dict(message="Delete successful."), 204
            return dict(message="issue with the name does not exist."), 404


class StreamResource(Resource):
    """Initialize handshake with client on sse subscription."""

    def get(self):
        subscribed_channels = ['default']
        pubsub = REDIS_CONN.pubsub()
        pubsub.subscribe(subscribed_channels)
        return Response(stream_with_context(stream(pubsub)),
                        content_type='text/event-stream')


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    api = Api(app)
    api.add_resource(IssueResource, '/api/issue/')
    api.add_resource(StreamResource, '/api/notification/')
    return app


app = create_app('development')

if __name__ == "__main__":
    app.run()
