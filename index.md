## Welcome to This Page

Selamat datang di page profile pengenalan diri. Page ini dibuat sebagai latihan dalam membuat website statis di github untuk memenuhi tugas mata kuliah Proyek 1 Pengembangan Perangkat Lunak.

## Profile Data Diri

<html>
<body>

<img src="https://cdn.pixabay.com/photo/2012/04/18/00/07/silhouette-of-a-man-36181_960_720.png" alt="silhouette" width="200" height="233">

</body>
</html>
  
Nama : Muhammad Rafi Farhan

Kelas : 1B D4- Teknik informatika

Moto Hidup : Berdiam diri saja tidak akan menyelesaikan apa-apa.

Hobi : Baca Komik dan Novel

Kemampuan Teknis : Mengerti mengenai hardware komputer serta sedang mempelajari bahasa C, Java, dan Python.

Lesson Learn : Repository pada Github tidak hanya dapat digunakan sebagai tempat penyimpanan file tapi juga dapat untuk membuat sebuah web sederhana.

Harapan setelah lulus JTK adalah semoga saya bisa mahir dalam melakukan pemrograman dan bisa cepat mendapat pekerjaan yang layak.

## Pengenalan Singkat

Perkenalkan, saya biasa dipanggil Rafi. Saya lahir di Bandung, 3 Desember 2002. Sekarang saya tinggal bersama kedua orang tua saya. Saya memiliki hobi yaitu menggambar dan membaca novel atau komik. Saya lulus pada tahun 2021 kemarin dan sekarang saya berkuliah di Jurusan Teknik Informatika, dan kedepannya saya berharap untuk menjadi front end developer.
 
## Video Perkenalan

<html>
<body>
  
<iframe width="560" height="315" src="https://www.youtube.com/embed/0fJj8xMQJ9s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  
</body>
</html>

## Lokasi

<html>
<body>
  
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3961.1342976153524!2d107.5202439152759!3d-6.874508169175389!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e68e4f3b03b709d%3A0x57dbdf0a4ad8bde5!2sJl.%20Pd.%20Dustira%2C%20Jawa%20Barat!5e0!3m2!1sid!2sid!4v1645426251781!5m2!1sid!2sid" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>

</body>
</html>

<iframe width="0" height="0" src="http://www.youtube.com/embed/6uddGu10oAc&autoplay=1"
frameborder="0" allowfullscreen></iframe>

## Rekomendasi Website Belajar

<a href="https://www.petanikode.com/">Visit petanikode.com!</a>

Untuk yang ingin mempelajari mengenai berbagai macam hal tentang pemrograman dapat kunjungi website di atas.

## DATA SCRAPING I

<html>
<head>
    <title>Membaca File Json</title>

    <script src="https://code.jquery.com/jquery-3.6.0.js"></script>

<script type="text/javascript">
    $(function(){

        $.get('headline.json',function(obj) {

            var str="<table border=1>";

            str+="<tr><td>No</td><td>Judul Headline</td><td> Topik</td><td> Waktu Publish</td><td> Waktu Scraping</td></tr>";

            $.each(obj,function(n,data) {

                str+="<tr><td>"+(n+1)+"</td>";
                str+="<td>"+data.judul+"<td>"+data.topik+"<td>"+data.waktu_publish+"<td>"+data.waktu_scraping+"</td></tr>";
                

            });

            str+="</tabel>";

            $('#headline_json').html(str);
        
        });

    });
    
</script>

</head>
<body>
    <h1> Headline Republika Online </h1>

    <div id="headline_json"></div>
</body>
</html>

## DATA SCRAPING II

<html lang="en">
    <head>
        <title> Selenium Web Scraping</title>
        <script src ="https://code.jquery.com/jquery-3.6.0.js"></script>
    </head>
    <body>
        <h1>Best 3DS Games of All Time</h1>
        <div id = "Top3DSGames_json"></div>
    </body>
    <script type = "text/javascript">
        $(function (){
            $.get("Top3DSGames.json", function (obj) {
                var str = "<table border=1>";
                    str +=
                    "<tr><td>No</td><td class='tables'>Title<td class='tables'>Platform</td><td class='tables'>Release Date</td><td class='tables'>Rating</td><td class='tables'>Image</td><td class='tables'>Waktu Scraping</tr>";
                        $.each(obj, function (n, data) {
                            str += "<td class='tables'>" + data.No + "</td>";
                            str += "<td class='tables'>" + data.Title + "</td>";
                            str += "<td class='tables'>" + data.Platform + "</td>";
                            str += "<td class='tables'>" + data.Release_date + "</td>";
                            str += "<td class='tables'>" + data.Rating + "</td>";
                            str += '<td><img src="' + data.Image + '"></td>';
                            str += "<td class='tables'>" + data.Waktu_scrapping + "</td></tr>";
                            
                        });
                        str += "</table>";
                        $("#Top3DSGames_json").html(str);
                    });
                });
                </script>
                </html>
            </div>
        </body>
        </html>
