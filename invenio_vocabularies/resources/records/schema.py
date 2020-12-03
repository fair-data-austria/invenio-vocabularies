from marshmallow import Schema
from marshmallow_utils.fields import Link
from uritemplate import URITemplate

from invenio_records_resources.resources import search_link_params, \
    search_link_when


class VocabularyLinksSchema(Schema):
    """Schema for a record's links."""

    # NOTE:
    #   - /api prefix is needed here because above are mounted on /api
    self_ = Link(
        template=URITemplate("/api/vocabularies/{pid_value}"),
        permission="read",
        params=lambda record: {'pid_value': record.pid.pid_value},
        data_key="self"  # To avoid using self since is python reserved key
    )


class SearchLinksSchema(Schema):
    """Schema for a search result's links."""

    # NOTE:
    #   - /api prefix is needed here because api routes are mounted on /api
    self = Link(
        template=URITemplate("/api/vocabularies{?params*}"),
        permission="search",
        params=search_link_params(0),
    )
    prev = Link(
        template=URITemplate("/api/vocabularies{?params*}"),
        permission="search",
        params=search_link_params(-1),
        when=search_link_when(-1)
    )
    next = Link(
        template=URITemplate("/api/vocabularies{?params*}"),
        permission="search",
        params=search_link_params(+1),
        when=search_link_when(+1)
    )