**cockroachdb**
<h1>penjelasan</h1>
<p>Basis data terdistribusi (distributed database) merupakan basis data yang perangkat-perangkat penyimpanannya terhubung dengan prosesor yang berbeda-beda. Salah satu atribut penting dari sebuah sistem basis data terdistribusi adalah meskipun sistem terdiri dari beberapa simpul (node), sistem harus tampak sebagai satu gugus (cluster) dari perspektif pengguna.
Sebuah sistem basis data terdistribusi berusaha menjawab paling sedikit tiga masalah berikut:
skalabilitas
ketersediaan (availability)
kehandalan (reliability)
Skalabilitas berkaitan dengan jumlah data dan transaksi yang mesti diproses oleh sistem. Ketersediaan berkaitan dengan uptime sistem yang idealnya harus selalu tersedia kapan pun pengguna butuh mengakses data dari sistem. Sementara kehandalan berkaitan dengan toleransi terhadap kerusakan (fault tolerance), bagaimana sistem tetap bisa melayani pengguna meski sebagian komponennya mengalami masalah.
Pada tulisan ini saya akan memaparkan pengalaman saya berkesperimen dengan salah satu teknologi basis data terdistribusi bernama CockroachDB. Dalam eksperimen yang akan kita simak bersama, saya akan mendemonstrasikan bagaimana CockroachDB menjawab persoalan skalabilitas, ketersediaan, dan kehandalan sebuah sistem.</p>

[Instalasi pada cockroachdb] (https://www.cockroachlabs.com/docs/stable/install-cockroachdb-windows.html)


**Replika Data**
<p>Pada eksperimen ini, kita akan mencoba bagaimana data direplikasi pada gugus basis data CockroachDB. Pertama, kita akan menggunakan data sampel yang disediakan oleh CockroachDB</p>

![](minggu-05/gambar1.jpg)

<p>memverifikasi bahwa data sampel sudah tersimpan</p>

![](minggu-05/gambar2.jpg)

<p>>akan memverifikasi bahwa data yang sama sudah direplikasi secara otomatis oleh CockroachDB ke simpul kedua dan ketiga </p>

![](minggu-05/gambar3.jpg)

