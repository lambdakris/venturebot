"""Streamlit app for MtnBot trip planner."""

import os

import streamlit as st
from typing import cast, Any
from pydantic import BaseModel

from client import MtnBotClient


class AppState(BaseModel):
    """Typed container for session state."""

    plan_data: dict | None = None
    plan_text: str | None = None
    error: str | None = None
    

def get_state() -> AppState:
    """Get or initialize typed session state."""
    if "app_state" not in st.session_state:
        st.session_state.app_state = AppState()
    return st.session_state.app_state


# Page config
st.set_page_config(
    page_title="MtnBot - Trip Planner",
    page_icon="🏔️",
    layout="wide",
)


@st.cache_resource
def get_client() -> MtnBotClient:
    """Initialize and cache the API client."""
    server_url = os.environ["SERVER_URL"]
    return MtnBotClient(base_url=server_url)


def main():
    st.title("🏔️ MtnBot - Trip Planner")
    st.markdown("*Transform your climbing ideas into comprehensive, safety-conscious trip plans.*")

    # Check API health
    client = get_client()

    state = get_state()

    st.divider()

    # Input section
    st.subheader("Trip Request")

    trip_request = st.text_area(
        label="Describe your trip",
        placeholder="Plan a winter climb of Mount Yale via East Ridge for January 25, 2026",
        height=100,
        label_visibility="collapsed",
    )

    generate_button = st.button("Generate Plan", type="primary", disabled=not trip_request)

    # Generation and output
    if generate_button and trip_request:
        with st.spinner("Planning trip... this may take a moment."):
            try:
                result = client.generate_plan(trip_request)

                state.plan_data = result["data"]
                state.plan_text = result["text"]
                state.error = None

            except Exception as e:
                state.error = str(e)
                state.plan_data = None
                state.plan_text = None

    # Display results
    if state.error:
        st.error(f"Error generating plan: {state.error}")

    elif state.plan_data:
        st.divider()

        # Header with download button
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("📋 Trip Plan")
        with col2:
            title = state.plan_data.get("title", "trip_plan")
            st.download_button(
                label="Download .md",
                data=str(state.plan_text),
                file_name=f"{title.replace(' ', '_')}.md",
                mime="text/markdown",
            )

        # Rendered markdown
        st.markdown(state.plan_text)

        # Structured data (collapsible)
        st.divider()
        with st.expander("🔧 Structured Data (debug)"):
            st.json(state.plan_data)


if __name__ == "__main__":
    main()
