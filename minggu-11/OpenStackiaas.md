<h2> OpenStack Infrasturkture as a Service ( IAAS ) </h2>

![image](https://user-images.githubusercontent.com/54845386/71346022-7a483d00-2599-11ea-8f39-2ab5583e50d0.png)

<h3>1. konsep IaaS</h3>
<p>Openstack adalah software opensource untuk menghandle cloud cumputing, openstack terkenal dalam penggunakan Infrasturkture as a Service (IAAS). openstack menjembatani dengan keterbatasan hardware secara fisik yang sulit untuk scalable resource, openstack dibangun dengan setidaknya minimal beberapa dedicated server dan network yang mumpuni, kemudian software openstack dapat memanajemen beberapa cloud infrastruktur yang scalable, pengguna openstack dapat memperbesar resource vCPU, memperbesar jumlah RAM, atau menambah Disk storage sampai ber Tera-tera :D tanpa memikirkan dedicated server/collocationnya. dengan openstack, kita serasa mempunyai private/public cloud sendiri.</p>

<h3>2. berbagai software IaaS</h3>

![image](https://user-images.githubusercontent.com/54845386/71346511-a7491f80-259a-11ea-935d-81f0d3a381c0.png)

![image](https://user-images.githubusercontent.com/54845386/71346564-c051d080-259a-11ea-9f6c-8c61e657ab32.png)

![image](https://user-images.githubusercontent.com/54845386/71346601-d19add00-259a-11ea-9c30-762d6b0002ce.png)

<h5>NOVA - Compute</h5>
<p>Compute Service yang bertugas membuat guest OS/Virtual Machine, Start VM, shutdown VM,reboot VM,destory VM. Nova hanyalah frontend bukan teknologi hypervisor seperti KVM, Xen dan lainnya. Untuk hypervisor-nya Nova bisa pakai backend Qemu, KVM, Xen, ataupun VMware vSphere.</p>

<h5>NEUTRON - Networking</h5>
<p>Neutron adalah layanan Openstack Networking as a Service atau NaaS. tugasnya me-manage jaringan virtual, floating ip address, security firewall. menggunakan neutron user tenant bisa buat jaringan virtual untuk tenant-nya, dia juga bisa buat router virtual termasuk port-nya, atur firewall, ip address, dan lainnya. Neutron banyak memanfaatkan komponen program Linux yang membentuk jadi Neutron. Dari Linux bridge, Open vSwitch, OpenFlow, Linux virtual ethernet, sampai Linux network namespace.</p>

<h5>SWIFT - Object Storage</h5>
<p>Swift adalah service object storage di OpenStack. berbeda dengan block storage, di object storage data yang disimpan disebut object, object ini punya metadata yang berisi informasi tentang object, seperti tipe filenya, besarnya berapa, dibuat kapan, dan sebagainya. Setiap object mempunyai id unik masing-masing. keunggulannya kapasitas object storage bisa di scalling bahkan sampai unlimited dan letak giografis fisik storage tidak menjadi masalah karena object storage melihatnya sebagai satu entity.</p>

<h5>GLANCE - Image Service</h5>
<p>Glance berfungsi memanage disk image. Disk image dapat diattach ke vm dari Nova, terus dipakai buat hard disk virtual. Glance seperti repositori disk image, user bisa upload disk image, dan menginstruksikan Nova supaya boot pakai disk image ini.</p>

<h5>KEYSTONE - Identity Service</h5>
<p>Keystone adalah identity service, sehingga semua service dan tenant di OpenStack harus terdaftar di Keystone. jika kita nambah service baru, misalkan Nova, maka Nova harus di daftarkan di Keystone. User/tenant juga harus didaftarkan ke Keystone. Keystone adalah service OpenStack yang berhubungan dengan Tenant, User, dan service lainnya.</p>

<h5>CINDER - Block Storage</h5>
<p>OpenStack Cinder adalah service block storage. berbeda dengan swift yang berbasis object, block storage dipakai sebagai hard disk virtual biasanya disebut volume. digunakan pada Storage Area Network atau SAN, dipakai pada filesystem di Guest OS. Block yang tersimpan di disk didistribusikan sebagai hard disk virtual ke server lewat protokol iSCSI atau Fibre Channel (FC)
disarikan dari : devnull.web.id</p>


<h3>3. getting started software IaaS yg dipilih</h3>
<p></p>

<h3>4. arsitektur dan konsep deployment pada software IaaS yg dipilih</h3>
<p></p>
