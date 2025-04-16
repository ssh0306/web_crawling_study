import requests
from datetime import datetime, timezone

def sync_time_with_server(url="https://artist.mnetplus.world/main/stg/izna"):
    # 요청 전 시간 (UTC)
    t1 = datetime.now(timezone.utc)

    # 서버에 GET 요청
    response = requests.get(url)
    server_date_str = response.headers.get("Date")

    # 요청 후 시간 (UTC)
    t2 = datetime.now(timezone.utc)

    # 서버 시간 파싱
    server_time = datetime.strptime(server_date_str, "%a, %d %b %Y %H:%M:%S GMT")
    server_time = server_time.replace(tzinfo=timezone.utc)

    # Round Trip Time (RTT)
    rtt = (t2 - t1).total_seconds()
    estimated_client_time_at_response = t1 + (t2 - t1) / 2

    # 시간 오차 계산
    time_offset = (server_time - estimated_client_time_at_response).total_seconds()

    print("=== 서버 시간 동기화 측정 ===")
    print(f"서버 시간 (UTC): {server_time}")
    print(f"클라이언트 추정 시간 (요청 중간): {estimated_client_time_at_response}")
    print(f"왕복 시간 (RTT): {rtt:.3f}초")
    print(f"추정 시간 오차: {time_offset:.3f}초")

sync_time_with_server()

#플챗
#시간 동기화 0.001초 이내
# === 서버 시간 동기화 측정 ===
# 서버 시간 (UTC): 2025-04-16 11:53:24+00:00
# 클라이언트 추정 시간 (요청 중간): 2025-04-16 11:53:24.084645+00:00
# 왕복 시간 (RTT): 0.234초
# 추정 시간 오차: -0.085초
