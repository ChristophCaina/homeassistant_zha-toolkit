# Constants related to parameters


# Constants representing input parameter keys
class USER_PARAMS_consts:
    __slots__ = ()
    CMD = "cmd"
    ENDPOINT = "endpoint"
    CLUSTER = "cluster"
    ATTRIBUTE = "attribute"
    ATTR_TYPE = "attr_type"
    ATTR_VAL = "attr_val"
    CODE = "code"
    MIN_INTRVL = "min_interval"
    MAX_INTRVL = "max_interval"
    REPTBLE_CHG = "reportable_change"
    DIR = "dir"
    MANF = "manf"
    TRIES = "tries"
    EXPECT_REPLY = "expect_reply"
    ARGS = "args"
    STATE_ID = "state_id"
    STATE_ATTR = "state_attr"
    ALLOW_CREATE = "allow_create"
    EVENT_SUCCESS = "event_success"
    EVENT_FAIL = "event_fail"
    EVENT_DONE = "event_done"
    FAIL_EXCEPTION = "fail_exception"
    READ_BEFORE_WRITE = "read_before_write"
    READ_AFTER_WRITE = "read_after_write"
    WRITE_IF_EQUAL = "write_if_equal"
    OUTCSV = "csvout"
    CSVLABEL = "csvlabel"


class SERVICE_consts:
    __slots__ = ()
    # General
    EXECUTE = "execute"
    # Specific
    ADD_GROUP = "add_group"
    ADD_TO_GROUP = "add_to_group"
    ALL_ROUTES_AND_NEIGHBOURS = "all_routes_and_neighbours"
    ATTR_READ = "attr_read"
    ATTR_WRITE = "attr_write"
    BACKUP = "backup"
    BIND_GROUP = "bind_group"
    BIND_IEEE = "bind_ieee"
    CONF_REPORT = "conf_report"
    CONF_REPORT_READ = "conf_report_read"
    EZSP_ADD_KEY = "ezsp_add_key"
    EZSP_BACKUP = "ezsp_backup"
    EZSP_CLEAR_KEYS = "ezsp_clear_keys"
    EZSP_GET_CONFIG_VALUE = "ezsp_get_config_value"
    EZSP_GET_IEEE_BY_NWK = "ezsp_get_ieee_by_nwk"
    EZSP_GET_KEYS = "ezsp_get_keys"
    EZSP_GET_POLICY = "ezsp_get_policy"
    EZSP_GET_TOKEN = "ezsp_get_token"  # nosec
    EZSP_GET_VALUE = "ezsp_get_value"
    EZSP_SET_CHANNEL = "ezsp_set_channel"
    EZSP_START_MFG = "ezsp_start_mfg"
    GET_GROUPS = "get_groups"
    GET_ROUTES_AND_NEIGHBOURS = "get_routes_and_neighbours"
    GET_ZLL_GROUPS = "get_zll_groups"
    ZHA_DEVICES = "zha_devices"
    HANDLE_JOIN = "handle_join"
    IEEE_PING = "ieee_ping"
    LEAVE = "leave"
    MISC_REINITIALIZE = "misc_reinitialize"
    OTA_NOTIFY = "ota_notify"
    REJOIN = "rejoin"
    REGISTER_SERVICES = "register_services"
    REMOVE_ALL_GROUPS = "remove_all_groups"
    REMOVE_FROM_GROUP = "remove_from_group"
    REMOVE_GROUP = "remove_group"
    SCAN_DEVICE = "scan_device"
    UNBIND_COORDINATOR = "unbind_coordinator"
    UNBIND_GROUP = "unbind_group"
    ZCL_CMD = "zcl_cmd"
    ZDO_FLOOD_PARENT_ANNCE = "zdo_flood_parent_annce"
    ZDO_JOIN_WITH_CODE = "zdo_join_with_code"
    ZDO_SCAN_NOW = "zdo_scan_now"
    ZDO_UPDATE_NWK_ID = "zdo_update_nwk_id"
    ZNP_BACKUP = "znp_backup"
    ZNP_NVRAM_BACKUP = "znp_nvram_backup"
    ZNP_NVRAM_RESET = "znp_nvram_reset"
    ZNP_NVRAM_RESTORE = "znp_nvram_restore"
    ZNP_RESTORE = "znp_restore"


# Constants representing internal parameters keys
class INTERNAL_PARAMS_consts:
    __slots__ = ()
    ALLOW_CREATE = "allow_create"
    ARGS = "args"
    ATTR_ID = "attr_id"
    ATTR_TYPE = "attr_type"
    ATTR_VAL = "attr_val"
    CLUSTER_ID = "cluster_id"
    CMD_ID = "cmd_id"
    CODE = "code"
    DIR = "dir"
    EP_ID = "endpoint_id"
    EVT_DONE = "event_done"
    EVT_FAIL = "event_fail"
    EVT_SUCCESS = "event_success"
    EXPECT_REPLY = "expect_reply"
    FAIL_EXCEPTION = "fail_exception"
    MANF = "manf"
    MAX_INTERVAL = "max_interval"
    MIN_INTERVAL = "min_interval"
    READ_AFTER_WRITE = "read_after_write"
    READ_BEFORE_WRITE = "read_before_write"
    REPORTABLE_CHANGE = "reportable_change"
    STATE_ATTR = "state_attr"
    STATE_ID = "state_id"
    TRIES = "tries"
    WRITE_IF_EQUAL = "write_if_equal"
    CSV_FILE = "csvfile"
    CSV_LABEL = "csvlabel"


INTERNAL_PARAMS = INTERNAL_PARAMS_consts()
USER_PARAMS = USER_PARAMS_consts()
SERVICES = SERVICE_consts()
