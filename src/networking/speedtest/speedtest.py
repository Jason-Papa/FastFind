import speedtest

def perform_speedtest():
    try:
        print("Performing speed test ...")
        # Initialize Speedtest object
        st = speedtest.Speedtest()

        # Get best server based on ping
        st.get_best_server()

        # Perform download and upload speed tests
        download_speed = st.download() / 1_000_000  # Convert from bits/s to Mbits/s
        upload_speed = st.upload() / 1_000_000      # Convert from bits/s to Mbits/s

        # Get the ping (latency)
        ping = st.results.ping

        # Display the results
        print(f"Download speed: {download_speed:.2f} Mbps")
        print(f"Upload speed: {upload_speed:.2f} Mbps")
        print(f"Ping: {ping:.2f} ms")

    except Exception as e:
        print(f"An error occurred: {e}")
