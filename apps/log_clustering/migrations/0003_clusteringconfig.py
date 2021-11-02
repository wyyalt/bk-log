# Generated by Django 2.2.6 on 2021-11-02 02:47

from django.db import migrations, models
import django_jsonfield_backport.models


class Migration(migrations.Migration):

    dependencies = [
        ("log_clustering", "0002_aiopssignatureandpattern"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClusteringConfig",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="创建时间")),
                ("created_by", models.CharField(default="", max_length=32, verbose_name="创建者")),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name="更新时间")),
                ("updated_by", models.CharField(blank=True, default="", max_length=32, verbose_name="修改者")),
                ("is_deleted", models.BooleanField(default=False, verbose_name="是否删除")),
                ("deleted_at", models.DateTimeField(blank=True, null=True, verbose_name="删除时间")),
                ("deleted_by", models.CharField(blank=True, max_length=32, null=True, verbose_name="删除者")),
                ("collector_config_id", models.IntegerField(blank=True, null=True, verbose_name="采集项id")),
                (
                    "collector_config_name_en",
                    models.CharField(blank=True, max_length=255, null=True, verbose_name="采集项英文名"),
                ),
                ("index_set_id", models.IntegerField(db_index=True, verbose_name="索引集id")),
                ("sample_set_id", models.IntegerField(blank=True, null=True, verbose_name="样本集id")),
                ("model_id", models.CharField(blank=True, max_length=128, null=True, verbose_name="模型id")),
                ("min_members", models.IntegerField(verbose_name="最小日志数量")),
                ("max_dist_list", models.CharField(max_length=128, verbose_name="敏感度")),
                ("predefined_varibles", models.TextField(verbose_name="预先定义的正则表达式")),
                ("delimeter", models.TextField(verbose_name="分词符")),
                ("max_log_length", models.IntegerField(verbose_name="最大日志长度")),
                ("is_case_sensitive", models.IntegerField(default=0, verbose_name="是否大小写忽略")),
                ("clustering_fields", models.CharField(max_length=128, verbose_name="聚合字段")),
                ("filter_rules", django_jsonfield_backport.models.JSONField(verbose_name="过滤规则")),
                ("bk_biz_id", models.IntegerField(verbose_name="业务id")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
