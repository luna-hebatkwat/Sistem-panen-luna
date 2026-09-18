```python
# Program Penghitung Total Hasil Panen

def hitung_total_panen(panen):
    return sum(panen)


def main():
    hasil_panen = [100, 150, 200, 125]

    total = hitung_total_panen(hasil_panen)

    print("Daftar hasil panen:", hasil_panen)
    print("Total hasil panen:", total, "kg")


if __name__ == "__main__":
    main()
```
