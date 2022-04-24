<?php

use yii\grid\GridView;
use yii\helpers\Html;

$this->title = 'Список задач';



?>
<div class="main-default-index">
    <h1><?= 'Мои задачи' ?></h1>
    <hr>
    <div style="width: 200px" class="mb-4">
        <?= Html::a('Создать задачу', '/create-task', ['class' => 'btn btn-primary btn-main']) ?>
    </div>


    <?= GridView::widget([
        'dataProvider' => $dataProvider,
        'filterModel' => $searchModel,
        'columns' => [
            [
                'label' => '№',
                'attribute' => 'id',
                'options' => ['width' => '70px'],
            ],
            [
                'label' => 'Название',
                'attribute' => 'title',
                'format' => 'html',
                'options' => ['width' => '150px'],
                'value' => function ($model) {
                    if (date('d-m-Y',$model->start_date) == date('d-m-Y') && $model->status == 'To Do')
                    {
                        return
                            '<div style="font-weight: bold; color: #b8b801">' .$model->title.'</div>';
                    } else {
                        return $model->title;
                    }
                }
            ],
            [
                'label' => 'Начало',
                'attribute' => 'start_date',
                'value' => function ($model) {
                    return date('d-m-Y',$model->start_date);
                }
            ],
            [
                'attribute' => 'due_date',
                'label' => 'Завершение',
                'format' => 'html',
                'value' => function ($model) {
                  if ((date('d-m-Y',$model->due_date) == date('d-m-Y')) && ($model->status == 'To Do') || $model->status == 'In Progress')
                  {
                      return
                            '<div style="font-weight: bold; color: darkred">' .date('d-m-Y',$model->due_date).'</div>';
                    } else {
                        return date('d-m-Y',$model->due_date);
                    }

//                    return date('d-m-Y',$model->due_date);
                }
            ],
            [
                'label' => 'Длительность, дней',
                'value' => function ($model) {
                    return $model->getEstimate();
                }
            ],
            [
                'label' => 'Описание',
                'attribute' => 'description'
            ],
            [
                'label' => 'Статус',
                'attribute' => 'status',
                'format' => 'html',
                'value' => function ($model) {
                    if (!empty($model->status) && $model->status !== 'Done') {
                        return $model->status. '<br>'.$model->changeStatus();
                    } else {
                        return '<div style="color: #136324; font-weight: bold">Выполнено!</div>';
                    }

                }
            ],
            [
                'label' => 'Действия',
                'format' => 'html',
                'value' => function ($model) {
                    return $model->getActions();
                }
            ]
        ]
    ]); ?>

</div>


