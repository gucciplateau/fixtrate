import enum


@enum.unique
class FixMsgType(enum.Enum):
    Heartbeat = b'0'
    TestRequest = b'1'
    ResendRequest = b'2'
    Reject = b'3'
    SequenceReset = b'4'
    Logout = b'5'
    Logon = b'A'
    IOI = b'6'
    Advertisement = b'7'
    ExecutionReport = b'8'
    OrderCancelReject = b'9'
    News = b'B'
    Email = b'C'
    NewOrderSingle = b'D'
    NewOrderList = b'E'
    OrderCancelRequest = b'F'
    OrderCancelReplaceRequest = b'G'
    OrderStatusRequest = b'H'
    Allocation = b'J'
    ListCancelRequest = b'K'
    ListExecute = b'L'
    ListStatusRequest = b'M'
    ListStatus = b'N'
    AllocationInstructionAck = b'P'
    DontKnowTrade = b'Q'
    QuoteRequest = b'R'
    Quote = b'S'
    SettlementInstructions = b'T'
    MarketDataRequest = b'V'
    MarketDataSnapshotFullRefresh = b'W'
    MarketDataIncrementalRefresh = b'X'
    MarketDataRequestReject = b'Y'
    QuoteCancel = b'Z'
    QuoteStatusRequest = b'a'
    QuoteAcknowledgement = b'b'
    SecurityDefinitionRequest = b'c'
    SecurityDefinition = b'd'
    SecurityStatusRequest = b'e'
    SecurityStatus = b'f'
    TradingSessionStatusRequest = b'g'
    TradingSessionStatus = b'h'
    MassQuote = b'i'
    BusinessMessageReject = b'j'
    BidRequest = b'k'
    BidResponse = b'l'
    ListStrikePrice = b'm'
    XMLnonFIX = b'n'
    RegistrationInstructions = b'o'
    RegistrationInstructionsResponse = b'p'
    OrderMassCancelRequest = b'q'
    OrderMassCancelReport = b'r'
    NewOrderCross = b's'
    CrossOrderCancelRequest = b'u'
    CrossOrderCancelReplaceRequest = b't'
    SecurityTypeRequest = b'v'
    SecurityTypes = b'w'
    SecurityListRequest = b'x'
    SecurityList = b'y'
    DerivativeSecurityListRequest = b'z'
    DerivativeSecurityList = b'AA'
    NewOrderMultileg = b'AB'
    MultilegOrderCancelReplaceRequest = b'AC'
    TradeCaptureReportRequest = b'AD'
    TradeCaptureReport = b'AE'
    OrderMassStatusRequest = b'AF'
    QuoteRequestReject = b'AG'
    RFQRequest = b'AH'
    QuoteStatusReport = b'AI'
    QuoteResponse = b'AJ'
    Confirmation = b'AK'
    PositionMaintenanceRequest = b'AL'
    PositionMaintenanceReport = b'AM'
    RequestForPositions = b'AN'
    RequestForPositionsAck = b'AO'
    PositionReport = b'AP'
    TradeCaptureReportRequestAck = b'AQ'
    TradeCaptureReportAck = b'AR'
    AllocationReport = b'AS'
    AllocationReportAck = b'AT'
    ConfirmationAck = b'AU'
    SettlementInstructionRequest = b'AV'
    AssignmentReport = b'AW'
    CollateralRequest = b'AX'
    CollateralAssignment = b'AY'
    CollateralResponse = b'AZ'
    CollateralReport = b'BA'
    CollateralInquiry = b'BB'
    NetworkCounterpartySystemStatusRequest = b'BC'
    NetworkCounterpartySystemStatusResponse = b'BD'
    UserRequest = b'BE'
    UserResponse = b'BF'
    CollateralInquiryAck = b'BG'
    ConfirmationRequest = b'BH'
    ContraryIntentionReport = b'BO'
    SecurityDefinitionUpdateReport = b'BP'
    SecurityListUpdateReport = b'BK'
    AdjustedPositionReport = b'BL'
    AllocationInstructionAlert = b'BM'
    ExecutionAcknowledgement = b'BN'
    TradingSessionList = b'BJ'
    TradingSessionListRequest = b'BI'
    SettlementObligationReport = b'BQ'
    DerivativeSecurityListUpdateReport = b'BR'
    TradingSessionListUpdateReport = b'BS'
    MarketDefinitionRequest = b'BT'
    MarketDefinition = b'BU'
    MarketDefinitionUpdateReport = b'BV'
    ApplicationMessageRequest = b'BW'
    ApplicationMessageRequestAck = b'BX'
    ApplicationMessageReport = b'BY'
    OrderMassActionReport = b'BZ'
    OrderMassActionRequest = b'CA'
    UserNotification = b'CB'
    StreamAssignmentRequest = b'CC'
    StreamAssignmentReport = b'CD'
    StreamAssignmentReportACK = b'CE'


@enum.unique
class MDEntryType(enum.Enum):
    BID = b'0'
    OFFER = b'1'
    TRADE = b'2'
    INDEX_VALUE = b'3'
    OPENING_PRICE = b'4'
    CLOSING_PRICE = b'5'
    SETTLEMENT_PRICE = b'6'
    TRADING_SESSION_HIGH_PRICE = b'7'
    TRADING_SESSION_LOW_PRICE = b'8'
    TRADING_SESSION_VWAP_PRICE = b'9'
    IMBALANCE = b'A'
    TRADE_VOLUME = b'B'
    OPEN_INTEREST = b'C'
    COMPOSITE_UNDERLYING_PRICE = b'D'
    SIMULATED_SELL_PRICE = b'E'
    SIMULATED_BUY_PRICE = b'F'
    MARGIN_RATE = b'G'
    MID_PRICE = b'H'
    EMPTY_BOOK = b'J'
    SETTLE_HIGH_PRICE = b'K'
    SETTLE_LOW_PRICE = b'L'
    PRIOR_SETTLE_PRICE = b'M'
    SESSION_HIGH_BID = b'N'
    SESSION_LOW_OFFER = b'O'
    EARLY_PRICES = b'P'
    AUCTION_CLEARING_PRICE = b'Q'
    SWAP_VALUE_FACTOR = b'S'
    DAILY_VALUE_ADJUSTMENT_FOR_LONG_POSITIONS = b'R'
    CUMULATIVE_VALUE_ADJUSTMENT_FOR_LONG_POSITIONS = b'T'
    DAILY_VALUE_ADJUSTMENT_FOR_SHORT_POSITIONS = b'U'
    CUMULATIVE_VALUE_ADJUSTMENT_FOR_SHORT_POSITIONS = b'V'
    RECOVERY_RATE = b'Y'
    RECOVERY_RATE_FOR_LONG = b'Z'
    RECOVERY_RATE_FOR_SHORT = b'a'
    FIXING_PRICE = b'W'
    CASH_RATE = b'X'


@enum.unique
class SubscriptionRequestType(enum.Enum):
    SNAPSHOT = b'0'
    SNAPSHOT_PLUS_UPDATES = b'1'
    DISABLE_PREVIOUS_SNAPSHOT_PLUS_UPDATE_REQUEST = b'2'


@enum.unique
class MDUpdateType(enum.Enum):
    FULL_REFRESH = b'0'
    INCREMENTAL_REFRESH = b'1'


@enum.unique
class MarketDepth(enum.Enum):
    FULL_BOOK = b'0'
    TOP_OF_BOOK = b'1'


@enum.unique
class EncryptMethod(enum.Enum):
    PKCS = b'1'
    DES = b'2'
    PKCS_DES = b'3'
    PGP_DES = b'4'
    PGP_DES_MD5 = b'5'
    PEM_DES_MD5 = b'6'
    NONE = b'0'


@enum.unique
class GapFillFlag(enum.Enum):
    NO = b'N'
    YES = b'Y'


@enum.unique
class BusinessRejectReason(enum.Enum):
    OTHER = b'0'
    UNKNOWN_ID = b'1'
    UNKNOWN_SECURITY = b'2'
    UNSUPPORTED_MESSAGE_TYPE = b'3'
    APPLICATION_NOT_AVAILABLE = b'4'
    CONDITIONALLY_REQUIRED_FIELD_MISSING = b'5'
    DELIVERTO_FIRM_NOT_AVAILABLE_AT_THIS_TIME = b'7'
    NOT_AUTHORIZED = b'6'
    INVALID_PRICE_INCREMENT = b'18'


@enum.unique
class TimeInForce(enum.Enum):
    DAY = b'0'
    GOOD_TILL_CANCEL = b'1'
    AT_THE_OPENING = b'2'
    IMMEDIATE_OR_CANCEL = b'3'
    FILL_OR_KILL = b'4'
    GOOD_TILL_CROSSING = b'5'
    GOOD_TILL_DATE = b'6'
    AT_THE_CLOSE = b'7'
    GOOD_THROUGH_CROSSING = b'8'
    AT_CROSSING = b'9'


@enum.unique
class OrdStatus(enum.Enum):
    NEW = b'0'
    PARTIALLY_FILLED = b'1'
    FILLED = b'2'
    DONE_FOR_DAY = b'3'
    CANCELED = b'4'
    REPLACED = b'5'
    PENDING_CANCEL_REPLACE = b'6'
    STOPPED = b'7'
    REJECTED = b'8'
    SUSPENDED = b'9'
    PENDING_NEW = b'A'
    CALCULATED = b'B'
    EXPIRED = b'C'
    ACCEPTED_FOR_BIDDING = b'D'
    PENDING_REPLACE = b'E'


@enum.unique
class OrdType(enum.Enum):
    MARKET = b'1'
    LIMIT = b'2'
    STOP = b'3'
    STOP_LIMIT = b'4'
    MARKET_ON_CLOSE = b'5'
    WITH_OR_WITHOUT = b'6'
    LIMIT_OR_BETTER = b'7'
    LIMIT_WITH_OR_WITHOUT = b'8'
    ON_BASIS = b'9'
    ON_CLOSE = b'A'
    LIMIT_ON_CLOSE = b'B'
    PREVIOUSLY_QUOTED = b'D'
    PREVIOUSLY_INDICATED = b'E'
    PEGGED = b'P'
    FUNARI = b'I'
    MARKET_IF_TOUCHED = b'J'
    MARKET_WITH_LEFTOVER_AS_LIMIT = b'K'
    PREVIOUS_FUND_VALUATION_POINT = b'L'
    NEXT_FUND_VALUATION_POINT = b'M'
    FOREX_MARKET = b'C'
    FOREX_LIMIT = b'F'
    FOREX_SWAP = b'G'
    FOREX_PREVIOUSLY_QUOTED = b'H'
    COUNTER_ORDER_SELECTION = b'Q'


@enum.unique
class Side(enum.Enum):
    BUY = b'1'
    SELL = b'2'


@enum.unique
class ExecInst(enum.Enum):
    STAY_ON_OFFERSIDE = b'0'
    NOT_HELD = b'1'
    WORK = b'2'
    GO_ALONG = b'3'
    OVER_THE_DAY = b'4'
    HELD = b'5'
    PARTICIPATE_DONT_INITIATE = b'6'
    STRICT_SCALE = b'7'
    TRY_TO_SCALE = b'8'
    STAY_ON_BIDSIDE = b'9'
    NO_CROSS = b'A'
    OK_TO_CROSS = b'B'
    CALL_FIRST = b'C'
    PERCENT_OF_VOLUME = b'D'
    DO_NOT_INCREASE = b'E'
    DO_NOT_REDUCE = b'F'
    ALL_OR_NONE = b'G'
    INSTITUTIONS_ONLY = b'I'
    LAST_PEG = b'L'
    MID_PRICE_PEG = b'M'
    NON_NEGOTIABLE = b'N'
    OPENING_PEG = b'O'
    MARKET_PEG = b'P'
    PRIMARY_PEG = b'R'
    SUSPEND = b'S'
    CUSTOMER_DISPLAY_INSTRUCTION = b'U'
    NETTING = b'V'
    FIXED_PEG_TO_LOCAL_BEST_BID_OR_OFFER_AT_TIME_OF_ORDER = b'T'
    PEG_TO_VWAP = b'W'
    REINSTATE_ON_SYSTEM_FAILURE = b'H'
    REINSTATE_ON_TRADING_HALT = b'J'
    CANCEL_ON_TRADING_HALT = b'K'
    CANCEL_ON_SYSTEM_FAILURE = b'Q'
    TRADE_ALONG = b'X'
    TRY_TO_STOP = b'Y'
    CANCEL_IF_NOT_BEST = b'Z'
    TRAILING_STOP_PEG = b'a'
    STRICT_LIMIT = b'b'
    IGNORE_PRICE_VALIDITY_CHECKS = b'c'
    PEG_TO_LIMIT_PRICE = b'd'
    WORK_TO_TARGET_STRATEGY = b'e'
    INTERMARKET_SWEEP = b'f'
    EXTERNAL_ROUTING_ALLOWED = b'g'
    EXTERNAL_ROUTING_NOT_ALLOWED = b'h'
    IMBALANCE_ONLY = b'i'
    SINGLE_EXECUTION_REQUESTED_FOR_BLOCK_TRADE = b'j'
    BEST_EXECUTION = b'k'
    SUSPEND_ON_SYSTEM_FAILURE = b'l'
    SUSPEND_ON_TRADING_HALT = b'm'
    REINSTATE_ON_CONNECTION_LOSS = b'n'
    CANCEL_ON_CONNECTION_LOSS = b'o'
    SUSPEND_ON_CONNECTION_LOSS = b'p'
    RELEASE_FROM_SUSPENSION = b'q'
    EXECUTE_AS_DELTA_NEUTRAL_USING_VOLATILITY_PROVIDED = b'r'
    EXECUTE_AS_DURATION_NEUTRAL = b's'
    EXECUTE_AS_FX_NEUTRAL = b't'


@enum.unique
class SessionRejectReason(enum.Enum):
    INVALID_TAG_NUMBER = b'0'
    REQUIRED_TAG_MISSING = b'1'
    SENDINGTIME_ACCURACY_PROBLEM = b'10'
    INVALID_MSGTYPE = b'11'
    XML_VALIDATION_ERROR = b'12'
    TAG_APPEARS_MORE_THAN_ONCE = b'13'
    TAG_SPECIFIED_OUT_OF_REQUIRED_ORDER = b'14'
    REPEATING_GROUP_FIELDS_OUT_OF_ORDER = b'15'
    INCORRECT_NUMINGROUP_COUNT_FOR_REPEATING_GROUP = b'16'
    NON_DATA_VALUE_INCLUDES_FIELD_DELIMITER = b'17'
    TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE = b'2'
    UNDEFINED_TAG = b'3'
    TAG_SPECIFIED_WITHOUT_A_VALUE = b'4'
    VALUE_IS_INCORRECT = b'5'
    INCORRECT_DATA_FORMAT_FOR_VALUE = b'6'
    DECRYPTION_PROBLEM = b'7'
    SIGNATURE_PROBLEM = b'8'
    COMPID_PROBLEM = b'9'
    OTHER = b'99'


@enum.unique
class ResetSeqNumFlag(enum.Enum):
    NO = b'N'
    YES = b'Y'


class FixTag(enum.IntEnum):
    AvgPx = 6
    BeginSeqNo = 7
    BeginString = 8
    BodyLength = 9
    CheckSum = 10
    ClOrdID = 11
    Commission = 12
    CommType = 13
    CumQty = 14
    EndSeqNo = 16
    ExecID = 17
    ExecInst = 18
    IOIID = 23
    LastPx = 31
    LastQty = 32
    MsgSeqNum = 34
    MsgType = 35
    NewSeqNo = 36
    OrderID = 37
    OrderQty = 38
    OrdStatus = 39
    OrdType = 40
    OrigClOrdID = 41
    OrigTime = 42
    PossDupFlag = 43
    Price = 44
    RefSeqNum = 45
    SenderCompID = 49
    SendingTime = 52
    Side = 54
    Symbol = 55
    TargetCompID = 56
    Text = 58
    TimeInForce = 59
    TransactTime = 60
    EncryptMethod = 98
    OrdRejReason = 103
    HeartBtInt = 108
    MinQty = 110
    TestReqID = 112
    GapFillFlag = 123
    ExpireTime = 126
    OnBehalfOfCompID = 115
    ResetSeqNumFlag = 141
    NoRelatedSym = 146
    LeavesQty = 151
    ExecType = 170
    StipulationValue = 234
    MDReqID = 262
    SubscriptionRequestType = 263
    MarketDepth = 264
    MDUpdateType = 265
    NoMDEntryTypes = 267
    NoMDEntries = 268
    MDEntryType = 269
    MDEntryPx = 270
    MDEntrySize = 271
    MDEntryTime = 273
    MDUpdateAction = 279
    MDReqRejReason = 281
    SecurityReqID = 320
    SecurityResponseID = 322
    RefTagID = 371
    RefMsgType = 372
    SessionRejectReason = 373
    BusinessRejectRefID = 379
    BusinessRejectReason = 380
    CommCurrency = 479
    SecurityRequestResult = 560
    SecurityListRequestType = 559
    LastLiquidityInd = 851


class FixVersion(enum.Enum):
    FIX42 = 'FIX.4.2'
    FIX44 = 'FIX.4.4'