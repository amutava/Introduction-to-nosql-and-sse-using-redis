"""Push services, based on  publish/subscribe model.

Utility module that implements Server-sent events (SSE) technology
Refrence:
    https://en.wikipedia.org/wiki/Server-sent_events
    https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
"""

import json
import redis
import time
import os


url = os.environ.get("REDIS_URL") or "redis://localhost:6379"
REDIS_CONN = redis.StrictRedis.from_url(url=url)


def stream(pubsub):
    """Stream generator: generate data to subscribed client via stream.

    Args:
      pubsub(Subscribe):listen for messages that get published to channels.

    yields:
      data(str): data sent to client
    """
    _30_MINS_IN_SECS = 30 * 60
    TIMEOUT = os.environ.get('TIMEOUT')
    TIMEOUT = int(TIMEOUT or _30_MINS_IN_SECS)
    start_time = time.time()

    for data in pubsub.listen():
        if data['type'] == 'message':
            msg = data['data'].decode("utf-8")
            yield msg
        elapsed_time = start_time - time.time()
        if TIMEOUT - elapsed_time < 0:
            yield 'data: closing stream.\n\n'
            return


def publish(data, channel='default', type='default', redis_conn=REDIS_CONN):
    """Push data to channel.

    Args:
      data(str): data to be pushed into channels
      channel(str): channel name, where to push data
      type(str): type of stream event, attouched to json_data
      redis_conn(str): connection to redis server

    Returns:
      int: number of clients that recived pushed data
    """
    data = formart_message(data, type)
    return redis_conn.publish(channel, data)


def formart_message(data, event_type='default', event_id=None):
        """Map a string to Event Stream Format.

        Args:
          data(any): data to be mappeds

        Returns:
           format_msg(str): data mapped to Event stream format
        """
        browser_reconnection_time = 10000
        # will allow client/browser to reconnect after 10 secs if connection is
        # lost

        json_data = json.dumps(data)
        format_msg = ''
        format_msg += 'id: {}\n'.format(event_id)
        format_msg += 'retry: {}\n'.format(browser_reconnection_time)
        format_msg += 'data: {}\n'.format(json_data)
        format_msg += 'event: {}\n'.format(event_type)
        return format_msg + '\n'
