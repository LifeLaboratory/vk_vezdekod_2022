<?php

use frontend\assets\AppAsset;
use yii\bootstrap4\Html;

AppAsset::register($this);
?>
<?php $this->beginPage() ?>
<!DOCTYPE html>
<html lang="<?= Yii::$app->language ?>" class="h-100">
<head>
    <meta charset="<?= Yii::$app->charset ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <?php $this->registerCsrfMetaTags() ?>
    <title><?= Html::encode($this->title) ?></title>
    <?php $this->head() ?>
</head>
<body class="d-flex flex-column h-100 radial-gradient-blue">
<?php $this->beginBody() ?>

<header>

</header>

<main role="main" class="flex-shrink-0">
    <div class="container">
        <div class="d-flex justify-content-center">
            <?= $content ?>
        </div>
    </div>
</main>
<style>
    .btn-main {
        border-color: #0a2f53;
        background: #0a2f53;
        width: 100%;
    }
    .btn-main:hover {
        border-color: #0a2f53;
        background: #0a2f53;
    }
    .radial-gradient-blue {
    background: radial-gradient(circle at 50% 50%,
    rgb(255, 255, 255) 50%,
    rgba(10, 47, 83, 0.04) 55%,
    rgba(10, 47, 83, 0.14) 70%,
    rgba(10, 47, 83, 0.2) 75%,
    rgba(10, 47, 83, 0.42) 87.5%,
    rgba(10, 47, 83, 0.62) 100%);
    }
    .container {
        padding: 100px 15px 20px !important;
    }
</style>

<?php $this->endBody() ?>
</body>
</html>
<?php $this->endPage();
