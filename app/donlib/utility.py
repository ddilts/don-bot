import datetime
import os


class Utility(object):
    """This is a collection of widely-used functions"""

    @classmethod
    def date_to_iso8601(cls, date_obj):
        """Returns an ISO8601-formatted string for datetime arg"""
        retval = date_obj.isoformat()
        return retval

    @classmethod
    def iso8601_arbitrary_days_ago(cls, days_ago):
        """Return ISO8601 datestamp for day ocurring `days_ago` days ago."""
        return Utility.date_to_iso8601(datetime.date.today() -
                                       datetime.timedelta(days=days_ago))

    @classmethod
    def iso8601_now(cls):
        """Return ISO 8601 UTC timestamp for now."""
        return Utility.date_to_iso8601(datetime.datetime.utcnow())

    @classmethod
    def iso8601_today(cls):
        """Return ISO 8601 datestamp for today."""
        return Utility.date_to_iso8601(datetime.date.today())

    @classmethod
    def iso8601_yesterday(cls):
        """Return ISO 8601 datestamp for yesterday."""
        return Utility.iso8601_arbitrary_days_ago(1)

    @classmethod
    def iso8601_one_week_ago(cls):
        """Return ISO 8601 datestamp for one week prior to today."""
        return Utility.iso8601_arbitrary_days_ago(7)

    @classmethod
    def iso8601_one_month_ago(cls):
        """In this case, we assume 30 days"""
        return Utility.iso8601_arbitrary_days_ago(30)

    @classmethod
    def event_is_critical(cls, event):
        """Return boolean, which represents criticality of event."""
        return event["critical"]

    @classmethod
    def is_suppressed_event_type(cls, config, event):
        """Return True if event should be suppressed."""
        sup_events = Utility.string_to_list(config.suppress_events)
        if event["type"] in sup_events:
            return True
        return False

    @classmethod
    def string_to_list(cls, events):
        return events.split(",")

    @classmethod
    def u_to_8601(cls, unixtime):
        """Return ISO 8601 timestamp for epoch time."""
        try:
            ret = datetime.datetime.fromtimestamp(float(unixtime)).isoformat()
        except TypeError:
            ret = "N/A"
        return ret

    @classmethod
    def bool_from_env(cls, envvar_name):
        """Return boolean for environment variable.

        If the value of environment variable indicated by envvar_name is
        "True" or "true", return boolean True. Anything else returns False.
        """
        envvar_value = os.getenv(envvar_name, "absent")
        if envvar_value in ["True", "true"]:
            envvar_bool = True
        else:
            envvar_bool = False
        return envvar_bool

    @classmethod
    def list_from_env(cls, envvar_name):
        """Return a list by splitting a environment variable by commas.

        If environment variable is empty, return an empty string.
        """
        return os.getenv(envvar_name, "").split(",")
