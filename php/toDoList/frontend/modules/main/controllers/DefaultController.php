<?php

namespace app\modules\main\controllers;

use app\models\Task;
use app\models\TaskSearch;
use Yii;
use yii\web\Controller;
use yii\web\NotFoundHttpException;

/**
 * Default controller for the `main` module
 */
class DefaultController extends Controller
{
    /**
     * Lists all Task models.
     *
     * @return string
     */
    public function actionIndex()
    {
        $searchModel = new TaskSearch();
        $dataProvider = $searchModel->search($this->request->queryParams);

        return $this->render('index', [
            'searchModel' => $searchModel,
            'dataProvider' => $dataProvider,
        ]);
    }

    public function actionCreate()
    {
        $model = new Task();

        if ($model->load(Yii::$app->request->post())) {
            $model->status = 'To Do';
            $model->save();
            return $this->redirect('/');
        } else {
            $model->loadDefaultValues();
        }

        return $this->render('create', [
            'model' => $model,
        ]);
    }

    public function actionUpdate($id)
    {
        $model = $this->findModel($id);

        if ($model->user_id == Yii::$app->user->identity->id) {

            if ($model->load(Yii::$app->request->post()) && $model->save()) {
                return $this->redirect('/');
            }

            return $this->render('update', [
                'model' => $model,
            ]);
        } else {
            return $this->redirect('/');
        }
    }

    public function actionChangeStatus($id)
    {
        $model = $this->findModel($id);


        if ($model->user_id == Yii::$app->user->identity->id) {

            $start_date = date('Y-m-d',$model->start_date);
            $due_date = date('Y-m-d',$model->due_date);
            if ($model->load(Yii::$app->request->post()) ) {
                $model->start_date = $start_date;
                $model->due_date = $due_date;
                $model->save();
                return $this->redirect('/');
            }

            return $this->render('change_status', [
                'model' => $model,
            ]);
        } else {
            return $this->redirect('/');
        }
    }

    public function actionDelete($id)
    {
       $model = $this->findModel($id)->delete();

        return $this->redirect(['/']);
    }

    protected function findModel($id)
    {
        if (($model = Task::findOne(['id' => $id])) !== null) {
            return $model;
        }

        throw new NotFoundHttpException('Model not found');
    }
}
