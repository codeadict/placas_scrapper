<!DOCTYPE html>
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

$placa = 'P000297';

exec('get_placa.py ' . $placa, $resp);

$data = json_decode($resp[0]);


echo "<h4>Fecha Inicio: " . $data->f_inicio . "</h4>";

#echo $data->placa;
?>
</body>
