import json
from abc import ABC
from typing import Union, Type, TypeVar, Optional

from ..utils.utils import parse_model
from .client import Client
from .payload import Payload

T = TypeVar('T')


class BaseAPI(ABC):
    """Base class for API operations with common request/response handling"""
    
    def __init__(self):
        self._client: Optional[Client] = None
        self._payload: Optional[Payload] = None
        self._error_code: Optional[int] = None
        self._error_msg: Optional[str] = None
    
    def _set_error(self, code: int, message: str):
        """Set error code and message"""
        self._error_code = code
        self._error_msg = message

    def _clear_error(self):
        """Clear error code and message"""
        self._error_code = None
        self._error_msg = None

    def successful(self, common_response):
        """Check if API response is successful"""
        try:
            if common_response is None:
                self._set_error(-1, "响应为空")
                return False
                
            if common_response.status != 200:
                self._set_error(common_response.status, common_response.message)
                return False

            if common_response.data.code != 0:
                self._set_error(common_response.data.code, common_response.data.message)
                return False

            self._clear_error()
            return True
        except Exception as e:
            self._set_error(-1, f"解析响应失败: {e}")
            return False

    @property
    def error_code(self) -> Optional[int]:
        """Get and clear error code"""
        ret = self._error_code
        self._error_code = None
        return ret

    @property
    def error_msg(self) -> Optional[str]:
        """Get and clear error message"""
        ret = self._error_msg
        self._error_msg = None
        return ret
    
    def _make_request(self, payload_data: dict, timeout: int = 0, is_async: bool = False) -> Union[str, bytes, None]:
        """
        Make a network request with the given payload.
        
        Args:
            payload_data: The payload dictionary to send
            timeout: Request timeout in seconds
            is_async: Whether to make an async request
            
        Returns:
            Response as string, bytes, or None
        """
        if not self._client:
            raise RuntimeError("Client not initialized")
            
        return self._client._network_request(
            json.dumps(payload_data), 
            timeout, 
            is_async
        )
    
    def _call_and_parse(self, response_class: Type[T], payload_method, *args, **kwargs) -> Optional[T]:
        """
        Make a request and parse the response into the specified model.
        
        Args:
            response_class: The response model class to parse into
            payload_method: The payload method to call
            *args, **kwargs: Arguments for the payload method
            
        Returns:
            Parsed response object or None
        """
        # Extract timeout and is_async if provided in kwargs
        timeout = kwargs.pop('_timeout', 0)
        is_async = kwargs.pop('_is_async', False)
        
        # Build payload
        payload_data = payload_method(*args, **kwargs)
        
        # Make request
        response = self._make_request(payload_data, timeout, is_async)
        
        if response is None:
            return None
            
        # Handle bytes response (e.g., screenshots)
        if isinstance(response, bytes):
            return response  # type: ignore
            
        # Parse JSON response
        try:
            response_dict = json.loads(response) if isinstance(response, str) else response
            return parse_model(response_class, response_dict)
        except (json.JSONDecodeError, ValueError) as e:
            # Log error if needed
            return None
