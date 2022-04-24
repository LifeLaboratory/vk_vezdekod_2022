<?php

/** @var yii\web\View $this */
/** @var yii\bootstrap4\ActiveForm $form */

use yii\bootstrap4\Html;
use yii\bootstrap4\ActiveForm;

$this->title = 'Вход в систему';
$this->params['breadcrumbs'][] = $this->title;
?>
<div class="site-login">
    <h1><?= Html::encode($this->title) ?></h1>

    <p>Введите ваши данные, чтобы войти:</p>


    <?php $form = ActiveForm::begin(['id' => 'login-form']); ?>

        <?= $form->field($model, 'username')->textInput(['autofocus' => true]) ?>

        <?= $form->field($model, 'password')->passwordInput() ?>

        <?= $form->field($model, 'rememberMe')->checkbox() ?>

        <div style="color:#999;margin:1em 0">
            Нет аккаунта? <?= Html::a('Зарегестрироваться', ['/signup']) ?>
        </div>

        <div class="form-group">
            <?= Html::submitButton('Войти', ['class' => 'btn btn-primary btn-main', 'name' => 'login-button']) ?>
        </div>

    <?php ActiveForm::end(); ?>

</div>