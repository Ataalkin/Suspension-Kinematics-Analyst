import numpy as np
import matplotlib.pyplot as plt

def analyze_suspension(wheel_travel, l_upper, l_lower, h_upright, track_width):
    # 1. Kamber Hesabı (Dinamik)
    camber_change = np.degrees(np.arctan(wheel_travel * (1/l_upper - 1/l_lower)))
    camber = -camber_change
    
    # 2. Roll Center Hesabı (Anlık Dönme Merkezi Metodu)
    # Basitleştirilmiş Geometri: Kolların kesişim noktasını buluyoruz
    # h_rc = (Track / 2) * tan(theta_lower)
    # Buradaki açı kolların boy farkına göre değişir.
    instant_center_dist = (l_lower * l_upper) / (l_lower - l_upper)
    rc_height = (track_width / 2) * (h_upright / instant_center_dist)
    
    return camber, rc_height

# --- INTERAKTIF GİRİŞ ---
print("\n" + "="*50)
print("🏎️  ADVANCED CHASSIS ANALYST v2.0 (ROLL CENTER)")
print("="*50)

try:
    L_upper = float(input("Üst Salıncak Boyu (mm - örn: 250): ") or 250)
    L_lower = float(input("Alt Salıncak Boyu (mm - örn: 400): ") or 400)
    H_upright = float(input("Taşıyıcı Yüksekliği (mm - örn: 300): ") or 300)
    Track = float(input("İz Genişliği (Track Width - mm - örn: 1600): ") or 1600)

    # Simülasyon: -50mm ile +50mm hareket
    travel_range = np.linspace(-50, 50, 100)
    results = [analyze_suspension(t, L_upper, L_lower, H_upright, Track) for t in travel_range]
    cambers = [r[0] for r in results]
    rc_heights = [r[1] for r in results]

    # --- GRAFİKLER ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Grafik 1: Kamber Kazanımı
    ax1.plot(travel_range, cambers, color='red', linewidth=2)
    ax1.set_title('Kamber Değişimi (Camber Gain)')
    ax1.set_xlabel('Tekerlek Hareketi (mm)')
    ax1.set_ylabel('Açı (Derece)')
    ax1.grid(True, linestyle=':')

    # Grafik 2: Roll Center Hareketi
    ax2.plot(travel_range, rc_heights, color='blue', linewidth=2)
    ax2.set_title('Roll Center Yüksekliği')
    ax2.set_xlabel('Tekerlek Hareketi (mm)')
    ax2.set_ylabel('Yükseklik (mm)')
    ax2.grid(True, linestyle=':')

    plt.tight_layout()
    print("\n📊 Porsche ayarları hazır, grafikler yükleniyor...")
    plt.show()

except Exception as e:
    print(f"Hata oluştu: {e}")