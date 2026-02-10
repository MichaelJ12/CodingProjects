<?php
class Database{

    public $connection;


    public function __destruct() {
        $this->connection = null;
    }
    
    
}
