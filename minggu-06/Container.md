<h1><b>BAGIAN KE-1</b></h1> 
Pengerjaan https://www.katacoda.com/courses/docker/deploying-first-container
<h3>Step 1 Running A Container</h3>

![step1](https://user-images.githubusercontent.com/54845386/71063067-8fd6f480-219e-11ea-94a0-624defe207e7.JPG)

<p>Mengidentifikasi nama Gambar Docker yang dikonfigurasi untuk menjalankan Redis. Dengan Docker, semua wadah dimulai berdasarkan Gambar Docker. Gambar-gambar ini berisi semua yang diperlukan untuk memulai proses; host tidak memerlukan konfigurasi atau dependensi.</p>
<p>CLI Docker memiliki perintah yang disebut run yang akan memulai wadah berdasarkan Gambar Docker. Strukturnya adalah buruh pelabuhan yang menjalankan <options> <image-name></p>
<p>Secara default, Docker akan menjalankan perintah di latar depan. Untuk berjalan di latar belakang, opsi -d harus ditentukan.

docker run -d redis</p>
<p>Secara default, Docker akan menjalankan versi terbaru yang tersedia. Jika versi tertentu diperlukan, itu dapat ditentukan sebagai tag, misalnya, versi 3.2 akan menjadi buruh pelabuhan run -d redis: 3.2.</p>

<h3>Step 2 - Finding Running Containers</h3>

![step2](https://user-images.githubusercontent.com/54845386/71064107-d75e8000-21a0-11ea-8c17-9ed7e9d432ee.JPG)

<p>Perintah ini juga menampilkan nama dan ID ramah yang dapat digunakan untuk mencari tahu informasi tentang masing-masing wadah.</p>

<h3>Step 3 - Accessing Redis</h3>

![step3](https://user-images.githubusercontent.com/54845386/71064318-6a97b580-21a1-11ea-8c70-05f9d0c62dbb.JPG)

<p>Setelah terbuka, dimungkinkan untuk mengakses proses seolah-olah itu berjalan pada OS host itu sendiri. </p>
<p>menjalankan Redis di latar belakang, dengan nama redisHostPort di port 6379 menggunakan perintah docker run -d --name redisHostPort -p 6379: 6379 redis: terbaru</p>
<p>Protip
Secara default, port pada host dipetakan ke 0.0.0.0, yang berarti semua alamat IP. Anda dapat menentukan alamat IP tertentu ketika Anda menentukan pemetaan port, misalnya, -p 127.0.0.1:6379:6379</p>

<h3>Step 4 - Accessing Redis</h3>

![step4](https://user-images.githubusercontent.com/54845386/71064539-e72a9400-21a1-11ea-8e96-c8f960b780a2.JPG)

<p>memungkinkannya untuk mengekspos Redis tetapi pada port yang tersedia secara acak. Dia memutuskan untuk menguji teorinya menggunakan docker run -d --name redisDynamic -p 6379 redis: terbaru</p>
<p>ditemukan melalui port docker redisDynamic 6379</p>
<p>Penentuan daftar kontainer informasi mapping docker ps</p>

<h3>Step 5 - Persisting Data</h3>

![step5](https://user-images.githubusercontent.com/54845386/71064797-89e31280-21a2-11ea-89e6-e4748a11f44e.JPG)

<p>Mengikat direktori (juga dikenal sebagai volume) dilakukan dengan menggunakan opsi -v <host-dir>: <container-dir>. Ketika direktori di-mount, file-file yang ada di direktori pada host dapat diakses oleh kontainer dan data apa pun yang diubah / ditulis ke direktori di dalam kontainer akan disimpan di host. Ini memungkinkan untuk meningkatkan atau mengganti wadah tanpa kehilangan data</p>

<h3>Step 6 - Running A Container In The Foreground</h3>

<p>memungkinkan untuk menimpa perintah yang digunakan untuk meluncurkan gambar. Mampu mengganti perintah default memungkinkan untuk memiliki satu gambar yang dapat digunakan kembali dalam berbagai cara. Sebagai contoh, gambar Ubuntu dapat menjalankan perintah OS atau menjalankan bash prompt interaktif menggunakan / bin / bash</p>
<p>Docker perintah menjalankan ubuntu ps meluncurkan wadah Ubuntu dan mengeksekusi perintah ps untuk melihat semua proses yang berjalan dalam wadah.</p>

<h1><b>BAGIAN KE-2</b></h1> 
https://www.katacoda.com/courses/docker/create-nginx-static-web-server

<h3>Step 1 - Create Dockerfile</h3>
<p>didefinisikan sebagai instruksi dalam Dockerfile. Gambar Docker dibangun berdasarkan konten Dockerfile. Dockerfile adalah daftar instruksi yang menjelaskan cara menggunakan aplikasi </p>

![Step1](https://user-images.githubusercontent.com/54845386/71065806-8b153f00-21a4-11ea-83cd-da34069cac25.JPG)

<h3>Step 2 - Build Docker Image</h3>

![Step2](https://user-images.githubusercontent.com/54845386/71065957-e21b1400-21a4-11ea-8591-70333c967904.JPG)

<p>Dockerfile digunakan oleh perintah pembangunan Docker CLI. Perintah build mengeksekusi setiap instruksi dalam Dockerfile. Hasilnya adalah Gambar Docker bawaan yang dapat diluncurkan dan menjalankan aplikasi yang dikonfigurasi.</p>

<h3>Step 3 - Run</h3>

![Step3](https://user-images.githubusercontent.com/54845386/71066680-b0ef1380-21a5-11ea-8723-fba02672a7c8.JPG)

<p>Membuka sebuah port dengan menggunakan nginx dan port host yang sudah di tentukan dengan menggunakan curl docker </p>

<h1><b>BAGIAN KE-3</b></h1> 
https://www.katacoda.com/courses/docker/2

<h3>Step 1 Base Images Dan Step 2 Running Commands </h3>

![Step1Dan2](https://user-images.githubusercontent.com/54845386/71067506-3a531580-21a7-11ea-948e-0144646ecfe0.JPG)

<p>menggunakan NGINX sebagai gambar dasar Dockerfile adalah file teks sederhana dengan perintah di setiap baris. Untuk mendefinisikan gambar dasar, menggunakan instruksi FROM </p>
<p>COPY <src> <dest> memungkinkan untuk menyalin file dari direktori yang berisi Dockerfile ke gambar wadah. Ini sangat berguna untuk kode sumber dan aset yang ingin digunakan di dalam wadah.</p>
  
<h3>Step 3 - Exposing Ports</h3>
<p>dapat diakses melalui port 80, tambahkan baris EXPOSE yang relevan ke Dockerfile.</p>

<h3>Step 4 - Default Commands</h3>
<p>menjalankan NGINX adalah nginx -g daemon off ;. Atur ini sebagai perintah default di Dockerfile.</p>

<h3>Step 5 - Building Containers</h3>
<p>Menggunakan perintah build docker untuk membangun gambar dapat memberi gambar nama dengan menggunakan opsi '-t <name>".</p>

![Step5](https://user-images.githubusercontent.com/54845386/71068531-7edfb080-21a9-11ea-83e5-208a0087a6de.JPG)

<h3>Step 6 - Launching New Image</h3>
<p>NGINX dirancang untuk dijalankan sebagai layanan latar belakang sehingga Anda harus menyertakan opsi -d. Untuk membuat server web dapat diakses, ikat ke port 80 menggunakan p 80:80</p>

![Step6](https://user-images.githubusercontent.com/54845386/71068698-d716b280-21a9-11ea-9032-c3d129cc6c93.JPG)
