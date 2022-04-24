<?php

/** @var \yii\web\View $this */
/** @var string $content */

use common\widgets\Alert;
use frontend\assets\AppAsset;
use yii\bootstrap4\Breadcrumbs;
use yii\bootstrap4\Html;
use yii\bootstrap4\Nav;
use yii\bootstrap4\NavBar;

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
<body class="d-flex flex-column h-100">
<?php $this->beginBody() ?>

<header>
    <?php
    NavBar::begin([
        'brandUrl' => '/',
        'options' => [
            'class' => 'navbar navbar-expand-md nav-bar-blue',
        ],
    ]);
    $menuItems = [
        ['label' => 'Главная', 'url' => ['/']],

    ];
    $menuItems[] = '<li>'
        . Html::beginForm(['/logout'], 'post', ['class' => 'form-inline'])
        . Html::submitButton(
            'Выйти (' . Yii::$app->user->identity->username . ')',
            ['class' => 'btn btn-link logout']
        )
        . Html::endForm()
        . '</li>';

    echo Nav::widget([
        'options' => ['class' => 'navbar-nav ml-auto'],
        'items' => $menuItems,
    ]);
    NavBar::end();
    ?>
</header>

<main role="main" class="flex-shrink-0">
    <div class="container">
        <?= $content ?>
    </div>
</main>

<style>
    .nav-bar-blue {
        background: #0a2f53;
    }
    .navbar-expand-md .navbar-nav .nav-link {
        color: white;
    }
    .btn-main {
        border-color: #0a2f53;
        background: #0a2f53;
        width: 100%;
    }
    .btn-main:hover {
        border-color: #0a2f53;
        background: #0a2f53;
    }
</style>
<?php $this->endBody() ?>
</body>
</html>
<?php $this->endPage();
