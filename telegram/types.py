# https://core.telegram.org/bots/api#available-types
from dataclasses import FrozenInstanceError, dataclass, field
from nested_dataclasses import nested
from typing import Optional, List
from .utils import nested_dataclass


@nested_dataclass
class User:
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    language_code: Optional[str] = None
    can_join_groups: Optional[bool] = None
    can_read_all_group_messages: Optional[bool] = None
    supports_inline_queries: Optional[bool] = None


@nested_dataclass
class ChatPhoto:
    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str


@nested_dataclass
class ChatPermissions:
    can_send_messages: Optional[bool] = None
    can_send_media_messages: Optional[bool] = None
    can_send_polls: Optional[bool] = None
    can_send_other_messages: Optional[bool] = None
    can_add_web_page_previews: Optional[bool] = None
    can_change_info: Optional[bool] = None
    can_invite_users: Optional[bool] = None
    can_pin_messages: Optional[bool] = None


@nested_dataclass
class Location:
    longitude: float
    latitude: float
    horizontal_accuracy: float
    live_period: int
    heading: int
    proximity_alert_radius: int


@nested_dataclass
class ChatLocation:
    location: Location
    address: str


@nested_dataclass
class PhotoSize:
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: Optional[int] = None


@nested_dataclass
class MaskPosition:
    point: str
    x_shift: float
    y_shift: float
    scale: float


@nested_dataclass
class Animation:
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: Optional[PhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


@nested_dataclass
class Audio:
    file_id: str
    file_unique_id: str
    duration: int
    performer: Optional[str] = None
    title: Optional[str] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None
    thumb: Optional[PhotoSize] = None


@nested_dataclass
class Document:
    file_id: str
    file_unique_id: str
    thumb: Optional[PhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


@nested_dataclass
class Sticker:
    file_id: str
    file_unique_id: str
    width: int
    height: int
    is_animated: bool
    thumb: Optional[PhotoSize] = None
    emoji: Optional[str] = None
    set_name: Optional[str] = None
    mask_position: Optional[MaskPosition] = None
    file_size: Optional[int] = None


@nested_dataclass
class Video:
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: Optional[PhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


@nested_dataclass
class VideoNote:
    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumb: Optional[PhotoSize] = None
    file_size: Optional[int] = None


@nested_dataclass
class Voice:
    file_id: str
    file_unique_id: str
    duration: int
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


@nested_dataclass
class LoginUrl:
    url: str
    forward_text: Optional[str] = None
    bot_username: Optional[str] = None
    request_write_access: Optional[bool] = None


@nested_dataclass
class CallbackGame:
    pass


@nested_dataclass
class InlineKeyboardButton:
    text: str
    url: Optional[str] = None
    login_url: Optional[LoginUrl] = None
    callback_data: Optional[str] = None
    switch_inline_query: Optional[str] = None
    switch_inline_query_current_chat: Optional[str] = None
    callback_game: Optional[CallbackGame] = None
    pay: Optional[bool] = None


@nested_dataclass
class InlineKeyboardMarkup:
    inline_keyboard: List[List[InlineKeyboardButton]] = None


@nested_dataclass
class MessageEntity:
    type: str
    offset: int
    length: int
    url: str
    user: User
    language: str


@nested_dataclass
class Contact:
    phone_number: str
    first_name: str
    last_name: Optional[str] = None
    user_id: Optional[int] = None
    vcard: Optional[str] = None


@nested_dataclass
class Dice:
    emoji: str
    value: int


@nested_dataclass
class Game:
    title: str
    description: str
    photo: List[PhotoSize]
    text: Optional[str] = None
    text_entities: Optional[List[MessageEntity]] = None
    animation: Optional[Animation] = None


@nested_dataclass
class PollOption:
    text: str
    voter_count: int


@nested_dataclass
class Poll:
    id: str
    question: str
    options: List[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    correct_option_id: Optional[int] = None
    explanation: Optional[str] = None
    explanation_entities: Optional[List[MessageEntity]] = None
    open_period: Optional[int] = None
    close_date: Optional[int] = None


@nested_dataclass
class Venue:
    location: Location
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    google_place_id: Optional[str] = None
    google_place_type: Optional[str] = None


@nested_dataclass
class MessageAutoDeleteTimerChanged:
    message_auto_delete_time: int


@nested_dataclass
class Invoice:
    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int


@nested_dataclass
class SuccessfulPayment:
    currency: str
    total_amount: int
    invoice_payload: str
    telegram_payment_charge_id: str
    provider_payment_charge_id: str
    shipping_option_id: Optional[str] = None
    order_info: Optional["OrderInfo"] = None


@nested_dataclass
class PassportData:
    pass  # not neccery TODO: Complete Later


@nested_dataclass
class ProximityAlertTriggered:
    traveler: User
    watcher: User
    distance: int


@nested_dataclass
class VoiceChatScheduled:
    start_date: int


@nested_dataclass
class VoiceChatStarted:
    pass


@nested_dataclass
class VoiceChatEnded:
    duration: int


@nested_dataclass
class VoiceChatParticipantsInvited:
    users: Optional[List[User]] = None


@nested_dataclass
class InlineQuery:
    id: str
    from_user: User
    query: str
    offset: str
    chat_type: Optional[str] = None
    location: Optional[Location] = None


@nested_dataclass
class ChosenInlineResult:
    result_id: str
    from_user: "User"
    query: str
    location: Optional[Location] = None
    inline_message_id: Optional[str] = None


@nested_dataclass
class ShippingAddress:
    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str


@nested_dataclass
class ShippingQuery:
    id: str
    from_user: "User"
    invoice_payload: str
    shipping_address: ShippingAddress


@nested_dataclass
class OrderInfo:
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    shipping_address: Optional[ShippingAddress] = None


@nested_dataclass
class PreCheckoutQuery:
    id: str
    from_user: "User"
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: Optional[str] = None
    order_info: Optional[OrderInfo] = None


@nested_dataclass
class PollAnswer:
    poll_id: str
    user: "User"
    option_ids: List[int]


class ChatMember:
    user: User
    status: str
    custom_title: str
    is_anonymous: Optional[bool] = None
    can_be_edited: Optional[bool] = None
    can_manage_chat: Optional[bool] = None
    can_post_messages: Optional[bool] = None
    can_edit_messages: Optional[bool] = None
    can_delete_messages: Optional[bool] = None
    can_manage_voice_chats: Optional[bool] = None
    can_restrict_members: Optional[bool] = None
    can_promote_members: Optional[bool] = None
    can_change_info: Optional[bool] = None
    can_invite_users: Optional[bool] = None
    can_pin_messages: Optional[bool] = None
    is_member: Optional[bool] = None
    can_send_messages: Optional[bool] = None
    can_send_media_messages: Optional[bool] = None
    can_send_polls: Optional[bool] = None
    can_send_other_messages: Optional[bool] = None
    can_add_web_page_previews: Optional[bool] = None
    until_date: Optional[int] = None


@nested_dataclass
class Chat:
    id: int
    type: str
    title: Optional[str] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    photo: Optional[ChatPhoto] = None
    bio: Optional[str] = None
    description: Optional[str] = None
    invite_link: Optional[str] = None
    pinned_message: Optional["Message"] = None
    permissions: Optional[ChatPermissions] = None
    slow_mode_delay: Optional[int] = None
    message_auto_delete_time: Optional[int] = None
    sticker_set_name: Optional[str] = None
    can_set_sticker_set: Optional[bool] = None
    linked_chat_id: Optional[int] = None
    location: Optional[ChatLocation] = None


@nested_dataclass
class ChatInviteLink:
    invite_link: str
    creator: User
    is_primary: bool
    is_revoked: bool
    expire_date: Optional[int] = None
    member_limit: Optional[int] = None


@nested_dataclass
class ChatMemberUpdated:
    chat: Chat
    from_user: User
    date: int
    old_chat_member: ChatMember
    new_chat_member: ChatMember
    invite_link: Optional[ChatInviteLink] = None


@nested_dataclass
class CallbackQuery:
    id: str
    from_user: User
    chat_instance: str
    message: Optional["Message"] = None
    inline_message_id: Optional[str] = None
    data: Optional[str] = None
    game_short_name: Optional[str] = None


@nested_dataclass
class Message:
    message_id: int
    date: int
    chat: Chat
    from_user: Optional[User] = None
    sender_chat: Optional[Chat] = None
    forward_from: Optional[User] = None
    forward_from_chat: Optional[Chat] = None
    forward_from_message_id: Optional[int] = None
    forward_signature: Optional[str] = None
    forward_sender_name: Optional[str] = None
    forward_date: Optional[int] = None
    reply_to_message: Optional["Message"] = None
    via_bot: Optional[User] = None
    edit_date: Optional[int] = None
    media_group_id: Optional[str] = None
    author_signature: Optional[str] = None
    text: Optional[str] = None
    entities: Optional[List[MessageEntity]] = None
    animation: Optional[Animation] = None
    audio: Optional[Audio] = None
    document: Optional[Document] = None
    photo: Optional[List[PhotoSize]] = None
    sticker: Optional[Sticker] = None
    video: 	Optional[Video] = None
    video_note: Optional[VideoNote] = None
    voice: Optional[Voice] = None
    caption: Optional[str] = None
    caption_entities: Optional[List[MessageEntity]] = None
    contact: Optional[Contact] = None
    dice: Optional[Dice] = None
    game: Optional[Game] = None
    poll: 	Optional[Poll] = None
    venue: Optional[Venue] = None
    location: Optional[Location] = None
    new_chat_members: Optional[List[User]] = None
    left_chat_member: Optional[User] = None
    new_chat_title: Optional[str] = None
    new_chat_photo: Optional[List[PhotoSize]] = None
    delete_chat_photo: Optional[bool] = None
    group_chat_created: Optional[bool] = None
    supergroup_chat_created: Optional[bool] = None
    channel_chat_created: Optional[bool] = None
    message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged] = None
    migrate_to_chat_id: Optional[int] = None
    migrate_from_chat_id: Optional[int] = None
    pinned_message: Optional["Message"] = None
    invoice: Optional[Invoice] = None
    successful_payment: Optional[SuccessfulPayment] = None
    connected_website: Optional[str] = None
    passport_data: Optional[PassportData] = None
    proximity_alert_triggered: Optional[ProximityAlertTriggered] = None
    voice_chat_scheduled: Optional[VoiceChatScheduled] = None
    voice_chat_started: Optional[VoiceChatStarted] = None
    voice_chat_ended: Optional[VoiceChatEnded] = None
    voice_chat_participants_invited: Optional[VoiceChatParticipantsInvited] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None


@nested_dataclass
class Update:
    update_id: int
    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    channel_post: Optional[Message] = None
    edited_channel_post: Optional[Message] = None
    inline_query: Optional[InlineQuery] = None
    chosen_inline_result: Optional[ChosenInlineResult] = None
    callback_query: Optional[CallbackQuery] = None
    shipping_query: Optional[ShippingQuery] = None
    pre_checkout_query: Optional[PreCheckoutQuery] = None
    poll: Optional[Poll] = None
    poll_awnser: Optional[PollAnswer] = None
    my_chat_memebr: Optional[ChatMemberUpdated] = None
    chat_member: Optional[ChatMemberUpdated] = None
