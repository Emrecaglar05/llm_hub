"""
Embedding Nedir, Nasıl Çıkarılır?
=====================================

Bu kod, sentence-transformers kütüphanesi kullanarak:
1. Metinlerden embedding çıkarma
2. Cosine similarity hesaplama
3. TSNE ile görselleştirme yapmayı gösterir

Gerekli Kütüphaneler:
pip install sentence-transformers scikit-learn matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import TSNE

# Adım 1: Model yükleme
print("📚 Sentence-Transformers modelini yüklüyoruz...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Adım 2: Örnek cümleler
sentences = [
    "Bugün hava çok güzel.",
    "Yarın yağmur yağacak.",
    "Kahve içmeyi seviyorum.",
    "Çay da güzel bir içecek.",
    "Python programlama dili çok kullanışlı.",
    "Machine learning ilginç bir alan.",
    "Kediler çok sevimli hayvanlar.",
    "Köpekler sadık dostlarımız.",
    "Müzik dinlemek rahatlatıcı.",
    "Kitap okumak bilgi arttırır."
]

print(f"\n📝 {len(sentences)} cümle ile çalışıyoruz:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")

# Adım 3: Embedding çıkarma
print("\n🔧 Embedding'ler çıkarılıyor...")
embeddings = model.encode(sentences)
print(f"✅ Embedding boyutu: {embeddings.shape}")
print(f"   Her cümle {embeddings.shape[1]} boyutlu vektör olarak temsil ediliyor")

# Adım 4: Cosine similarity hesaplama
print("\n📊 Cosine similarity matrisi hesaplanıyor...")
similarity_matrix = cosine_similarity(embeddings)

# En benzer cümle çiftini bulma
print("\n🔍 En benzer cümle çiftleri:")
max_similarity = 0
best_pair = (0, 0)

for i in range(len(sentences)):
    for j in range(i+1, len(sentences)):
        similarity = similarity_matrix[i][j]
        if similarity > max_similarity:
            max_similarity = similarity
            best_pair = (i, j)
        print(f"Cümle {i+1} - Cümle {j+1}: {similarity:.3f}")

print(f"\n🏆 EN BENZER ÇİFT:")
print(f"Cümle {best_pair[0]+1}: '{sentences[best_pair[0]]}'")
print(f"Cümle {best_pair[1]+1}: '{sentences[best_pair[1]]}'")
print(f"Benzerlik skoru: {max_similarity:.3f}")

# Adım 5: TSNE ile 2D görselleştirme
print("\n🎨 TSNE ile 2D görselleştirme hazırlanıyor...")

# TSNE ile boyut azaltma
tsne = TSNE(n_components=2, random_state=42, perplexity=5)
embeddings_2d = tsne.fit_transform(embeddings)

# Görselleştirme
plt.figure(figsize=(12, 8))
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], 
           c=range(len(sentences)), cmap='tab10', s=100, alpha=0.7)

# Her nokta için cümle numarasını etiket olarak ekle
for i, (x, y) in enumerate(embeddings_2d):
    plt.annotate(f'{i+1}', (x, y), xytext=(5, 5), 
                textcoords='offset points', fontsize=12, fontweight='bold')

plt.title('Cümle Embedding\'lerinin 2D TSNE Görselleştirmesi', fontsize=16, fontweight='bold')
plt.xlabel('TSNE Boyut 1', fontsize=12)
plt.ylabel('TSNE Boyut 2', fontsize=12)
plt.grid(True, alpha=0.3)

# Renk barı ekle
cbar = plt.colorbar()
cbar.set_label('Cümle Numarası', fontsize=12)

plt.tight_layout()
plt.savefig('/Users/yaseminarslan/Desktop/buildwithllmsbootcamp/hafta_4/images/embedding_visualization.png', 
            dpi=300, bbox_inches='tight')
plt.show()

# Adım 6: Özet bilgiler
print("\n📋 ÖZET:")
print("="*50)
print(f"• Toplam cümle sayısı: {len(sentences)}")
print(f"• Embedding boyutu: {embeddings.shape[1]}")
print(f"• En benzer çift: Cümle {best_pair[0]+1} ve {best_pair[1]+1}")
print(f"• En yüksek benzerlik: {max_similarity:.3f}")
print(f"• Görselleştirme kaydedildi: embedding_visualization.png")

print("\n🎯 Embedding'ler hakkında:")
print("• Embedding'ler, metinlerin sayısal vektör temsilleridir")
print("• Benzer anlamlı metinler, benzer embedding vektörlerine sahiptir")
print("• Cosine similarity, iki vektör arasındaki açısal benzerliği ölçer")
print("• TSNE, yüksek boyutlu veriyi 2D'de görselleştirmeye yarar")


"""
✅ 5. Kodun Genel Akışı
Sentence-Transformers modeli yükleniyor.
10 örnek cümle belirleniyor.
Bu cümlelerden embedding çıkarılıyor.
Cosine similarity hesaplanıyor ve en benzer çift bulunuyor.
t-SNE ile embedding’ler görselleştiriliyor.
Özet bilgiler konsola yazdırılıyor.
"""