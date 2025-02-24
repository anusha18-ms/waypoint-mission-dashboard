import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Waypoint Mission Dashboard")

tab = st.sidebar.radio("Select a Tab", ["Home", "Mission Logs", "3D Map", "AI Story", "Saved Missions", "Leaderboard"])

if tab == "Home":
    st.title("🚀 Waypoint Mission Dashboard")
    st.write("Welcome! Select a tab to start.")

elif tab == "Mission Logs":
    st.title("📂 Upload & View Missions")
    uploaded_file = st.file_uploader("Upload Flight Log (CSV)", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

elif tab == "3D Map":
    st.title("🌍 Interactive 3D Waypoint Visualization with DSM Coordinates")

    # Sample waypoint data 
    df = pd.DataFrame({
    "Waypoint": ["WP1", "WP2", "WP3", "WP4"],
    "Latitude": [37.7749, 37.7755, 37.7760, 37.7765],
    "Longitude": [-122.4194, -122.4198, -122.4201, -122.4205],
    "Altitude": [100, 120, 110, 130],
    "DSM": ["6G CC 50872 83109", "6G CC 50874 83115", "6G CC 50875 83112", "6G CC 50877 83118"],
    "Image": ["images_resized/wp1.jpg", "images_resized/wp2.jpg", "images_resized/wp3.jpg", "images_resized/wp4.jpg"]
})

    # Add detailed hover tooltip
    df["Info"] = df.apply(lambda row: f"<b>{row.Waypoint}</b><br>"
                                      f"DSM: {row.DSM}<br>"
                                      f"Lat: {row.Latitude}, Lon: {row.Longitude}<br>"
                                    f"Altitude: {row.Altitude} ft", axis=1)


    # 3D Visualization Plotly
    fig = go.Figure(go.Scatter3d(
    x=df["Longitude"],
    y=df["Latitude"],
    z=df["Altitude"],
    mode='markers+lines',
    marker=dict(size=7, color="#fc0303", opacity=0.9),
    line=dict(width=4, color="#32a852"),
    hovertext=df["Info"],
    hoverinfo="text"
    ))

    fig.update_layout(scene=dict(
    xaxis_title="Longitude",
    yaxis_title="Latitude",
    zaxis_title="Altitude (ft)"
    ), margin=dict(l=0, r=0, b=0, t=30))

    st.plotly_chart(fig, use_container_width=True)

    # Waypoint Image Viewer
    st.subheader("📸 Waypoint Image Viewer")

    selected_waypoint = st.selectbox("Select a Waypoint to view image:", df["Waypoint"])

    if selected_waypoint:
      image_path = df[df["Waypoint"] == selected_waypoint]["Image"].values[0]
      st.image(image_path, caption=f"Image from {selected_waypoint}", use_container_width=True)


elif tab == "AI Story":
    st.title("🧠 AI Mission Story")
    st.write("AI-generated mission summary will be displayed here.")

elif tab == "Saved Missions":
    st.title("💾 Load Saved Waypoints")
    st.write("Pilots can load previously saved waypoint missions.")

elif tab == "Leaderboard":
    st.title("🏆 Leaderboard - Top Pilots")
    st.write("This will show rankings based on mission efficiency.")
