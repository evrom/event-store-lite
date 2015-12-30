This package provides an event store service with pluggable handling to post events to subscribers.

This event store requires interfaces defined in `event-store-lite.domain.models`
* `Store` provides the storage mechanism for events
* `Post` sends the event to subscribers

These are provided to the application via dependency injection.

Included in this application is a SQLite implementation of `Store` and a HTTP client implementation of `Post`

## Recieving from event emitters

This service uses HTTP server to recieve events from emitters. Emitters make a POST request with the event in whatever formatting. A unique id is generated for the event by the `Store` implementation and retrieved with the `get_event_id` method. The `content-type`, `path`, and `body` of the POST request and the event ID are stored in respective fields in the `Store` implementation. The `post_to_subscribers` method is called on the `Post` implementation, and an HTTP response is returned with the event ID.


