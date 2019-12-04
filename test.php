<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class AddColumnFlagToTsFundScaleTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('ts_fund_scale', function (Blueprint $table) {
            $table->tinyInteger('flag')->after('ts_ratio');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::table('ts_fund_scale', function (Blueprint $table) {
           $table->dropColumn('flag');
        });
    }
}
