import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from sessions.session_content import render_session

def render():
    render_session("s14")
