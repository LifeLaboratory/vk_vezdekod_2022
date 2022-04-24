<div class="admin-users-create">
    <h1>Создать задачу</h1>
    <hr>
    <div class="col-lg-6 col-12">
        <?php use yii\helpers\Html;
        use yii\widgets\ActiveForm;

        $form = ActiveForm::begin(); ?>

        <?= $form->field($model, 'title')->textInput(['autofocus' => true]) ?>
        <?= $form->field($model, 'start_date')->textInput(['type' => 'date', 'min' => date('Y-m-d'),'max' => '2023-00-00']) ?>

        <?= $form->field($model, 'due_date')->textInput(['type' => 'date', 'min' => date('Y-m-d'), 'max' => '2023-00-00']) ?>
        <?= $form->field($model, 'description')->textarea() ?>

        <?= Html::submitButton('Создать', ['class' => 'btn btn-primary btn-main', 'name' => 'create-user-button']) ?>


        <?php ActiveForm::end(); ?>

    </div>
</div>
<style>
    .control-label {
        font-weight: bold;
        color: #27235a
    }
    .help-block {
        color: darkred;
    }
</style>
