

<div class="admin-users-create">
    <h1>Изменить статус: <?= $model->title ?></h1>
    <hr>
    <div class="col-lg-6 col-12">
        <?php use yii\helpers\Html;
        use yii\widgets\ActiveForm;

        $form = ActiveForm::begin(); ?>

        <?= $form->field($model, 'status')
            ->dropDownList([
                    'To Do' => 'Запланировано',
                    'In Progress' => 'В работе',
                    'Done' => 'Выполнено'
            ])



        ?>

        <?= Html::submitButton('Сохранить', ['class' => 'btn btn-primary btn-main', 'name' => 'create-user-button']) ?>


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
