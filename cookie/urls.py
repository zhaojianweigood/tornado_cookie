"""Specifies mappings between URLs and handlers.

   .. versionchanged: 4.5
      `URLSpec` is now a subclass of a `Rule` with `PathMatches` matcher and is preserved for
      backwards compatibility.
    Parameters:

    def __init__(
            self,
            pattern: Union[str, Pattern],
            handler: Any,
            kwargs: Dict[str, Any] = None,
            name: str = None,
    ) -> None:

    * ``pattern``: Regular expression to be matched. Any capturing
      groups in the regex will be passed in to the handler's
      get/post/etc methods as arguments (by keyword if named, by
      position if unnamed. Named and unnamed capturing groups
      may not be mixed in the same rule).

    * ``handler``: `~.web.RequestHandler` subclass to be invoked.

    * ``kwargs`` (optional): A dictionary of additional arguments
      to be passed to the handler's constructor.

    * ``name`` (optional): A name for this handler.  Used by
      `~.web.Application.reverse_url`.

    """
from tornado.web import url

from cookie.views import IndexHandler


urlpatterns = [
    url(r'/', IndexHandler),
]
