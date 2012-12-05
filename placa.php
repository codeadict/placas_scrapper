<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />

     <!-- Set the viewport width to device width for mobile -->
     <meta name="viewport" content="width=device-width" />
    <title>Obtener Datos de Seguro</title>

    <!-- Fix HTML5 Tags on MS monsters-->
    <!--[if lt IE 9]>
    <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
</head>
<body>
<?php
$placa = escapeshellcmd($_POST['placa']);

echo $_POST['placa'];

exec('get_placa.py ' . $placa, $resp);

$data = json_decode($resp[0]);

echo "<h1>Datos de la Placa Ingresada</H1>";

echo "<h4>Numero de Placa: " . $data->placa . "</h4>";
echo "<h4>Aseguradora: " . $data->aseguradora . "</h4>";
echo "<h4>Número de Certificado: " . $data->no_certificado . "</h4>";
echo "<h4>Fecha Inicio: " . $data->f_inicio . "</h4>";
echo "<h4>Fecha Fin: " . $data->f_fin . "</h4>";
echo "<h4>Fecha Vigencia: " . $data->vigencia . "</h4>";
?>
<br/>
Running on <a href="http://python.org">Python</a>
</body>
</html>
