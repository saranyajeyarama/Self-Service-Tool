# import os
# import base64
# import hashlib
# import secrets
# from typing import Optional
# import msal
# import streamlit as st
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# class AzureADAuth:
#     def __init__(self):
#         self.client_id = os.getenv('AZURE_CLIENT_ID')
#         self.tenant_id = os.getenv('AZURE_TENANT_ID', 'common')
#         self.authority = f'https://login.microsoftonline.com/{self.tenant_id}/'
#         # Define scopes as a list of strings
#         self.scope = ['https://graph.microsoft.com/User.Read']  # Basic Microsoft Graph scope
#         self.redirect_path = os.getenv('REDIRECT_PATH', '').rstrip('/')  # Remove trailing slash
        
#         if not self.client_id:
#             raise ValueError("Azure AD credentials not properly configured. Please check your .env file.")

#         self._msal_app = msal.PublicClientApplication(
#             client_id=self.client_id,
#             authority=self.authority,
#             client_credential=None  # Explicitly set for public client
#         )
    
#     def _generate_code_verifier(self) -> str:
#         """Generate a code verifier for PKCE."""
#         token = secrets.token_bytes(32)
#         code_verifier = base64.urlsafe_b64encode(token).decode('utf-8')
#         return code_verifier.rstrip('=')  # Remove padding
    
#     def _generate_code_challenge(self, code_verifier: str) -> str:
#         """Generate a code challenge for PKCE."""
#         sha256_hash = hashlib.sha256(code_verifier.encode('utf-8')).digest()
#         code_challenge = base64.urlsafe_b64encode(sha256_hash).decode('utf-8')
#         return code_challenge.rstrip('=')  # Remove padding
    
#     def get_auth_url(self) -> str:
#         """Generate the authorization URL for SSO login with PKCE."""
#         # Generate and store PKCE values
#         code_verifier = self._generate_code_verifier()
#         code_challenge = self._generate_code_challenge(code_verifier)
        
#         # Store code_verifier in session state for later use
#         st.session_state['code_verifier'] = code_verifier
        
#         # Generate state parameter if not exists
#         if 'state' not in st.session_state:
#             st.session_state.state = secrets.token_urlsafe(32)
        
#         auth_params = {
#             'response_type': 'code',
#             'code_challenge': code_challenge,
#             'code_challenge_method': 'S256'
#         }
        
#         auth_url = self._msal_app.get_authorization_request_url(
#             scopes=self.scope,
#             redirect_uri=self._get_redirect_uri(),
#             state=st.session_state.state,
#             prompt='select_account',  # Force account selection
#             **auth_params
#         )
#         return auth_url
    
#     def process_auth_code(self, auth_code: str) -> Optional[dict]:
#         """Process the authorization code and get access token using PKCE."""
#         try:
#             # Retrieve code_verifier from session state
#             code_verifier = st.session_state.get('code_verifier')
#             if not code_verifier:
#                 raise ValueError("Code verifier not found in session state")
                
#             result = self._msal_app.acquire_token_by_authorization_code(
#                 code=auth_code,
#                 scopes=self.scope,
#                 redirect_uri=self._get_redirect_uri(),
#                 code_verifier=code_verifier
#             )
            
#             if 'error' in result:
#                 raise ValueError(f"Error acquiring token: {result.get('error_description', result['error'])}")
                
#             return result
#         finally:
#             # Clear PKCE values from session state
#             if 'code_verifier' in st.session_state:
#                 del st.session_state['code_verifier']
#             if 'state' in st.session_state:
#                 del st.session_state.state
    
#     def _get_redirect_uri(self) -> str:
#         """Get the full redirect URI."""
#         return self.redirect_path

# def init_auth():
#     """Initialize authentication state."""
#     if 'auth' not in st.session_state:
#         st.session_state.auth = AzureADAuth()
#     if 'user' not in st.session_state:
#         st.session_state.user = None


import os
import base64
import hashlib
import secrets
from typing import Optional
import msal
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AzureADAuth:
    def __init__(self):
        self.client_id = os.getenv('AZURE_CLIENT_ID')
        self.tenant_id = os.getenv('AZURE_TENANT_ID', 'common')
        self.authority = f'https://login.microsoftonline.com/{self.tenant_id}'
        # Define scopes as a list of strings
        self.scope = ['https://graph.microsoft.com/User.Read']  # Basic Microsoft Graph scope
        self.redirect_path = os.getenv('REDIRECT_PATH')
        
        if not self.client_id:
            raise ValueError("Azure AD credentials not properly configured. Please check your .env file.")

        self._msal_app = msal.PublicClientApplication(
            client_id=self.client_id,
            authority=self.authority,
            token_cache=None  # Disable token cache for public client
            )
    
    def _generate_code_verifier(self) -> str:
        """Generate a code verifier for PKCE."""
        code_verifier = secrets.token_urlsafe(32)
        return code_verifier
    
    def _generate_code_challenge(self, code_verifier: str) -> str:
        """Generate a code challenge for PKCE."""
        code_challenge = base64.urlsafe_b64encode(
            hashlib.sha256(code_verifier.encode('utf-8')).digest()
        ).decode('utf-8').rstrip('=')
        return code_challenge
    
    def get_auth_url(self) -> str:
        """Generate the authorization URL for SSO login with PKCE."""
        # Generate PKCE values
        code_verifier = self._generate_code_verifier()
        code_challenge = self._generate_code_challenge(code_verifier)
        
        # Store code_verifier in session state
        st.session_state['code_verifier'] = code_verifier
        
        # Generate state parameter
        st.session_state['state'] = secrets.token_urlsafe(32)
        
        # Prepare auth parameters
        auth_params = {
            'response_type': 'code',
            'code_challenge': code_challenge,
            'code_challenge_method': 'S256'
        }
        
        auth_url = self._msal_app.get_authorization_request_url(
            scopes=self.scope,
            redirect_uri=self._get_redirect_uri(),
            state=st.session_state['state'],
            **auth_params
        )
        return auth_url
    
    def process_auth_code(self, auth_code: str) -> Optional[dict]:
        """Process the authorization code and get access token using PKCE."""
        try:
            code_verifier = st.session_state.get('code_verifier')
            if not code_verifier:
                raise ValueError("Code verifier not found in session state")
            
            result = self._msal_app.acquire_token_by_authorization_code(
                code=auth_code,
                scopes=self.scope,
                redirect_uri=self._get_redirect_uri(),
                code_verifier=code_verifier,
                pkce=True
            )
            
            if 'error' in result:
                raise ValueError(f"Error acquiring token: {result.get('error_description', result['error'])}")
            
            return result
        finally:
            # Clean up PKCE values
            st.session_state.pop('code_verifier', None)
            st.session_state.pop('state', None)
    
    def _get_redirect_uri(self) -> str:
        """Get the full redirect URI."""
        return self.redirect_path

def init_auth():
    """Initialize authentication state."""
    if 'auth' not in st.session_state:
        st.session_state.auth = AzureADAuth()
    if 'user' not in st.session_state:
        st.session_state.user = None