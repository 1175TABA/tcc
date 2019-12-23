<h2>Docker Compose</h2>
<p>Dengan docker dapat menyimpan konfigurasi dalam file, berarti semua perubahan dependency service, seperti versi database dan service lain dapat dimasukkan dalam VCS (Version Control System). Dengan VCS kita dapat lebih mudah men-debug jika terjadi error pada software
Docker / Container Orchestration ini sebenarnya adalah mengurus daur hidup dari container-container yang ada, yang ada dalam environment yang dinamik. Contoh orchestrator yang dikenal kalangan masyarakat luas, salah satunya adalah kubernetes, atau docker swarm.</p>

![image](https://user-images.githubusercontent.com/54845386/71370068-48f26000-25df-11ea-87d7-cbc02435a90a.png)

<p>Cara kerja Docker orchestrator pod IP address bertugas untuk menyimpan container-container yang dipakai oleh host tersebut, lalu di kontainer tersebut, interaksi antar kontainer dalam docker orchestration dijalankan via service third party, sehingga service tersebut dapat meregulasi usage image file dalam kontainer.</p>

<h2></h2>
<p>Ada beberapa cara kerja docker orchestration :</p>
<p>-	Membuat dan mendeploy dari container yang sudah ada</p>
<p>-	Redundancy dari container</p>
<p>-	Mengatur load dari setiap docker</p>
<p>-	Pemindahan host jika dari host yang di gunakan itu mati</p>
<p>-	Alokasi resources</p>
<p>-	Melihat tampilan detail servis yang jalan</p>
<p>-	Memonitoring</p>
<p>-	Konfigurasi dari aplikasi yang menjalankan docker</p>

