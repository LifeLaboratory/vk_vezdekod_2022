<?php

namespace app\modules\auth;

/**
 * auth module definition class
 */
class Module extends \yii\base\Module
{
    /**
     * {@inheritdoc}
     */
    public $controllerNamespace = 'app\modules\auth\controllers';

    /**
     * {@inheritdoc}
     */
    public function init()
    {
        $this->layout = 'auth';
        parent::init();

        // custom initialization code goes here
    }
}
