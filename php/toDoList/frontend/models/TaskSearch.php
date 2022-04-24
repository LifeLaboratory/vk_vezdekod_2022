<?php

namespace app\models;

use common\models\User;
use Yii;
use yii\base\Model;
use yii\data\ActiveDataProvider;

class TaskSearch extends Task
{
    public function rules()
    {
        return [
            [['id', 'user_id'], 'integer'],
            [['title'], 'safe']
        ];
    }

    public function attributeLabels()
    {
        return [
            'title' => 'Название',
            'start_date' => 'Дата начала',
            'due_date' => 'Дата окончания',
            'estimate' => 'Время выполнения',
            'description' => 'Описание',

        ];
    }


    public function scenarios()
    {
        // bypass scenarios() implementation in the parent class
        return Model::scenarios();
    }

    public function search($params)
    {
        $query = Task::find()
            ->where(['user_id' => 1])
            ->orderBy('id desc');

        $dataProvider = new ActiveDataProvider([
            'query' => $query,
        ]);

        $this->load($params);

        if (!$this->validate()) {
            // uncomment the following line if you do not want to return any records when validation fails
            // $query->where('0=1');
            return $dataProvider;
        }


        $query->andFilterWhere([
            'id' => $this->id,
        ]);

        $query
            ->andFilterWhere(['like', 'title', $this->title])
            ->andFilterWhere(['like', 'description', $this->description]);
        return $dataProvider;
    }
}

?>
