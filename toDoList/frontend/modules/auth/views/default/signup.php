<?php

use yii\bootstrap4\Html;
use yii\bootstrap4\ActiveForm;

$this->title = 'Регистрация';
$this->params['breadcrumbs'][] = $this->title;
?>
<div class="site-signup">
    <h1><?= Html::encode($this->title) ?></h1>

    <p>Заполните полните поля, чтобы зарегистрироваться:</p>

    <?php $form = ActiveForm::begin(['id' => 'form-signup']); ?>

        <?= $form->field($model, 'nickname')->textInput(['autofocus' => true]) ?>

        <?= $form->field($model, 'username')->textInput(['autofocus' => true]) ?>

        <?= $form->field($model, 'email') ?>

        <?= $form->field($model, 'password')->passwordInput() ?>

        <div class="form-group">
            <?= Html::submitButton('Зарегестрироваться', ['class' => 'btn btn-primary btn-main', 'name' => 'signup-button']) ?>
        </div>

    <div style="color:#999;margin:1em 0">
       Уже зарегестрированы? <?= Html::a('Войти', ['/login']) ?>
    </div>

    <?php ActiveForm::end(); ?>

</div>