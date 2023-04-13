# Pacmann-SuperStoreApp

Repo ini dibangun sebagai tugas akhir materi python pacmann.

## Latar Belakang
Dibutuhkan suatu sistem self service untuk cashier yang dimana sistem dapat melakukan aktifitas CRUD dengan melibatkan customer sebagai aktor dari sistemnya, bukan petugas
kasir. Adapun aktifitas sistem sebagai berikut
 - menginputkan / memasukan barang kedalam keranjang
 - mengubah detail barang
 - menghapus barang
 - melihat isi keranjang
 - mereset isi keranjang

## Requirenments
Untuk menunjang terbentuknya aplikasi self service cashier ini, dibutuhkan suatu alur dari setiap aktifitas yang telah dibuat hingga menjadi seperti dibawah
 - Pembuatan ID
  ID diperuntukan sebagai identitas keranjang yang dimiliki oleh setiap customer. ID dibuat menggunakan bantuan ```UUID``` yang dimana ID diperoleh secara otomatis ketika 
program dijalankan. Selengkapnya dijelaskan pada diagram alur dibawah.
  ![Generate ID Transactions drawio](https://user-images.githubusercontent.com/42725407/231838446-883834b3-b2be-4d3b-b226-ae8fac627281.png)
 - Menambahkan Barang
  Customer diperbolehkan untuk menambahkan barang seusai yang mereka inginkan serta sebanyak apapun yang mereka mau. Aktifitas ini terdapat pada fungsi ```add_items```. Fungsi tersebut membutuhkan satu parameter
  yaitu ```item_list``` yang berisi item apa yang diinputkan oleh customer dan dikemas dalam bentuk dictionary yang dikemas lagi kedalam list. Selengkapnya dijelaskan pada diagram alur dibawah.
  ![Add Item Transactions drawio](https://user-images.githubusercontent.com/42725407/231840309-f0a490fb-b601-4a66-b832-785dcf05b01d.png)
 - Mengubah detail barang
  Customer diperbolehkan untuk mengubah isi keranjang yang dimiliki. Aktifitas ini terdapat pada fungsi ```edit_item```. Fungsi tersebut membutuhkan beberapa parameter seperti
    - ```name``` : nama barang yang akan di update
    - ```item``` : nama baru untuk item yang dipilih. parameter boleh tidak diisi / default ```False```
    - ```count``` : nilai baru untuk jumlah barang. parameter boleh tidak diisi / default ```False```
    - ```price``` : nilai baru untuk harga barang. parameter boleh tidak diisi / default ```False```
  ```name``` diperlukan sistem untuk memperoleh item mana yang akan di ubah. Sistem akan mencari terlebih dahulu apakah item yang diinginkan tersedia didalam keranjang atau tidak. 
  Selain paramater itu jika parameter terisi makan sistem akan mengindikasikan bagian mana yang akan diubah dari barang tersebut. Selengkapnya dijelaskan pada diagram alur dibawah.
  ![Update Items drawio](https://user-images.githubusercontent.com/42725407/231843038-f1274d35-19dc-4190-a4e6-9e90f78f1e8b.png)
 - Menghapus Barang
  Customer diperbolehkan untuk menghapus barang yang dimiliki didalam keranjang. Aktifitas ini terdapat pada fungsi ```delete_item```. Fungsi tersebut membutuhkan satu parameter
  yaitu ```item``` yang berisi item apa yang akan dihapus oleh customer. Sistem akan mencari terlebih dahulu apakah item yang diinginkan tersedia didalam keranjang atau tidak.
  Selengkapnya dijelaskan pada diagram alur dibawah.
  ![Delete Items drawio](https://user-images.githubusercontent.com/42725407/231845527-a8ffe1f1-6efb-4ec5-a852-6328aca427e8.png)
 - Reset Keranjang
  Customer diperbolehkan untuk menghapus barang yang dimiliki didalam keranjang dengan menggunakan fungsi ```reset_item```. Fungsi ini akan menghapus semua isi keranjang.
  
  
  
  
  
  
  
  
