pengeluaran = []

print("=== Catatan Pengeluaran Sekolah (2 Minggu / 14 Hari) ===")

for hari in range(1, 15):
    jumlah = float(input(f"Masukkan pengeluaran hari ke-{hari} (Rp): "))
    pengeluaran.append(jumlah)

total = sum(pengeluaran)
rata = total / len(pengeluaran)

print("\n=== Ringkasan Pengeluaran ===")
for i, nilai in enumerate(pengeluaran, start=1):
    print(f"Hari ke-{i}: Rp{nilai:,.0f}")

print(f"\nTotal pengeluaran selama 2 minggu: Rp{total:,.0f}")
print(f"Rata-rata pengeluaran per hari: Rp{rata:,.0f}")