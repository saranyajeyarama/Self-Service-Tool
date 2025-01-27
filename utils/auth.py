import os
from typing import Optional
import msal
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AzureADAuth:
    def __init__(self):
        self.client_id = os.getenv('AZURE_CLIENT_ID')
        self.client_secret = os.getenv('AZURE_CLIENT_SECRET')
        self.tenant_id = os.getenv('AZURE_TENANT_ID', 'common')
        self.authority = f'https://login.microsoftonline.com/{self.tenant_id}/'
        self.scope = ['User.Read']
        self.redirect_path = os.getenv('REDIRECT_PATH')
        
        if not self.client_id or not self.client_secret:
            raise ValueError("Azure AD credentials not properly configured. Please check your .env file.")

        self._msal_app = msal.ConfidentialClientApplication(
            client_id=self.client_id,
            client_credential=self.client_secret,
            authority=self.authority
        )
    
    def get_auth_url(self) -> str:
        """Generate the authorization URL for SSO login."""
        auth_url = self._msal_app.get_authorization_request_url(
            scopes=self.scope,
            redirect_uri=self._get_redirect_uri(),
            state=st.session_state.get('state', '')
        )
        return auth_url
    
    def process_auth_code(self, auth_code: str) -> Optional[dict]:
        """Process the authorization code and get access token."""
        result = self._msal_app.acquire_token_by_authorization_code(
            code=auth_code,
            scopes=self.scope,
            redirect_uri=self._get_redirect_uri()
        )
        return result
    
    def _get_redirect_uri(self) -> str:
        """Get the full redirect URI."""
        base_url = st.get_option('server.baseUrlPath')
        if base_url.endswith('/'):
            base_url = base_url[:-1]
        return f"{base_url}{self.redirect_path}"

def init_auth():
    """Initialize authentication state."""
    if 'auth' not in st.session_state:
        st.session_state.auth = AzureADAuth()
    if 'user' not in st.session_state:
        st.session_state.user = None        