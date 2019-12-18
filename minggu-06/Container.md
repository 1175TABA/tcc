<h1>Sedikit Membahas</h1>
<p>Apa itu Docker?
Docker menggambarkan diri mereka sebagai "platform terbuka bagi pengembang dan sysadmin untuk membangun, mengirim, dan menjalankan aplikasi terdistribusi".
Docker memungkinkan Anda untuk menjalankan kontainer. Wadah adalah proses berpasir yang menjalankan aplikasi dan ketergantungannya pada sistem operasi host. Aplikasi di dalam wadah menganggap dirinya sebagai satu-satunya proses yang berjalan pada mesin sementara mesin dapat menjalankan beberapa wadah secara mandiri.</p>

<h1>Step 1 Running A Container</h1>

![step1](https://user-images.githubusercontent.com/54845386/71063067-8fd6f480-219e-11ea-94a0-624defe207e7.JPG)

<p>Mengidentifikasi nama Gambar Docker yang dikonfigurasi untuk menjalankan Redis. Dengan Docker, semua wadah dimulai berdasarkan Gambar Docker. Gambar-gambar ini berisi semua yang diperlukan untuk memulai proses; host tidak memerlukan konfigurasi atau dependensi.</p>
<p>CLI Docker memiliki perintah yang disebut run yang akan memulai wadah berdasarkan Gambar Docker. Strukturnya adalah buruh pelabuhan yang menjalankan <options> <image-name></p>
<p>Secara default, Docker akan menjalankan perintah di latar depan. Untuk berjalan di latar belakang, opsi -d harus ditentukan.

docker run -d redis</p>
<p>Secara default, Docker akan menjalankan versi terbaru yang tersedia. Jika versi tertentu diperlukan, itu dapat ditentukan sebagai tag, misalnya, versi 3.2 akan menjadi buruh pelabuhan run -d redis: 3.2.</p>

<h1>Step 2 - Finding Running Containers</h1>

![step2](https://user-images.githubusercontent.com/54845386/71064107-d75e8000-21a0-11ea-8c17-9ed7e9d432ee.JPG)

<p>Perintah ini juga menampilkan nama dan ID ramah yang dapat digunakan untuk mencari tahu informasi tentang masing-masing wadah.</p>

<h1>Step 3 - Accessing Redis</h1>

![step3](https://user-images.githubusercontent.com/54845386/71064318-6a97b580-21a1-11ea-8c70-05f9d0c62dbb.JPG)

<p>Setelah terbuka, dimungkinkan untuk mengakses proses seolah-olah itu berjalan pada OS host itu sendiri. </p>
<p>menjalankan Redis di latar belakang, dengan nama redisHostPort di port 6379 menggunakan perintah docker run -d --name redisHostPort -p 6379: 6379 redis: terbaru</p>
<p>Protip
Secara default, port pada host dipetakan ke 0.0.0.0, yang berarti semua alamat IP. Anda dapat menentukan alamat IP tertentu ketika Anda menentukan pemetaan port, misalnya, -p 127.0.0.1:6379:6379</p>

<h1>Step 4 - Accessing Redis</h1>

![step4](https://user-images.githubusercontent.com/54845386/71064539-e72a9400-21a1-11ea-8e96-c8f960b780a2.JPG)

<p>memungkinkannya untuk mengekspos Redis tetapi pada port yang tersedia secara acak. Dia memutuskan untuk menguji teorinya menggunakan docker run -d --name redisDynamic -p 6379 redis: terbaru</p>
<p>ditemukan melalui port docker redisDynamic 6379</p>
<p>Penentuan daftar kontainer informasi mapping docker ps</p>

<h1>Step 5 - Persisting Data</h1>

![step5](https://user-images.githubusercontent.com/54845386/71064797-89e31280-21a2-11ea-89e6-e4748a11f44e.JPG)

<p>Mengikat direktori (juga dikenal sebagai volume) dilakukan dengan menggunakan opsi -v <host-dir>: <container-dir>. Ketika direktori di-mount, file-file yang ada di direktori pada host dapat diakses oleh kontainer dan data apa pun yang diubah / ditulis ke direktori di dalam kontainer akan disimpan di host. Ini memungkinkan untuk meningkatkan atau mengganti wadah tanpa kehilangan data</p>

<h1>Step 6 - Running A Container In The Foreground</h1>

<p>memungkinkan Anda untuk menimpa perintah yang digunakan untuk meluncurkan gambar. Mampu mengganti perintah default memungkinkan untuk memiliki satu gambar yang dapat digunakan kembali dalam berbagai cara. Sebagai contoh, gambar Ubuntu dapat menjalankan perintah OS atau menjalankan bash prompt interaktif menggunakan / bin / bash</p>
<p>Docker perintah menjalankan ubuntu ps meluncurkan wadah Ubuntu dan mengeksekusi perintah ps untuk melihat semua proses yang berjalan dalam wadah.</p>


<p></p>
<p></p>
