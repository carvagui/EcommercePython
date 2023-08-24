
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itempedido',
            options={'verbose_name': 'Item do pedido', 'verbose_name_plural': 'Itens do pedido'},
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='user',
            new_name='usuario',
        ),
    ]
