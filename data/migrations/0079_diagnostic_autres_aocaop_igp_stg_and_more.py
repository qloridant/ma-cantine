# Generated by Django 4.0.5 on 2022-06-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0078_alter_purchase_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostic',
            name='autres_aocaop_igp_stg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, AOC / AOP / IGP / STG'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='autres_bio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, Bio'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='autres_commerce_equitable',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, Commerce équitable'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='autres_equivalents',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, Produits équivalents'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='autres_externalites',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, Produit prenant en compte les coûts imputés aux externalités environnementales pendant son cycle de vie'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='autres_fermier',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, Fermier'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='autres_france',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, Provenance France'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='autres_hve',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, Haute valeur environnementale'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='autres_label_rouge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, Label rouge'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='autres_local',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, Produit local'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='autres_peche_durable',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, Pêche durable'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='autres_performance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, Produits acquis sur la base de leurs performances en matière environnementale'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='autres_rup',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, Région ultrapériphérique'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='autres_short_distribution',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Autres produits frais, surgelés et d’épicerie, Circuit-court'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_aocaop_igp_stg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, AOC / AOP / IGP / STG'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_bio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, Bio'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_commerce_equitable',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, Commerce équitable'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_equivalents',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, Produits équivalents'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_externalites',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, Produit prenant en compte les coûts imputés aux externalités environnementales pendant son cycle de vie'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_fermier',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, Fermier'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_france',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, Provenance France'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_hve',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, Haute valeur environnementale'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_label_rouge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, Label rouge'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_local',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, Produit local'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_peche_durable',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, Pêche durable'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_performance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, Produits acquis sur la base de leurs performances en matière environnementale'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_rup',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, Région ultrapériphérique'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boissons_short_distribution',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boissons, Circuit-court'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_aocaop_igp_stg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, AOC / AOP / IGP / STG'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_bio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, Bio'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_commerce_equitable',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, Commerce équitable'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_equivalents',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, Produits équivalents'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_externalites',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, Produit prenant en compte les coûts imputés aux externalités environnementales pendant son cycle de vie'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_fermier',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, Fermier'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_france',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, Provenance France'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_hve',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, Haute valeur environnementale'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_label_rouge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, Label rouge'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_local',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, Produit local'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_peche_durable',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, Pêche durable'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_performance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, Produits acquis sur la base de leurs performances en matière environnementale'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_rup',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, Région ultrapériphérique'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='boulangerie_short_distribution',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Boulangerie/Pâtisserie fraîches, Circuit-court'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_aocaop_igp_stg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, AOC / AOP / IGP / STG'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_bio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, Bio'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_commerce_equitable',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, Commerce équitable'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_equivalents',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, Produits équivalents'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_externalites',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, Produit prenant en compte les coûts imputés aux externalités environnementales pendant son cycle de vie'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_fermier',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, Fermier'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_france',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, Provenance France'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_hve',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, Haute valeur environnementale'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_label_rouge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, Label rouge'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_local',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, Produit local'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_peche_durable',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, Pêche durable'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_performance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, Produits acquis sur la base de leurs performances en matière environnementale'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_rup',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, Région ultrapériphérique'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_de_la_mer_short_distribution',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Produits aquatiques frais et surgelés, Circuit-court'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_aocaop_igp_stg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), AOC / AOP / IGP / STG'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_bio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), Bio'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_commerce_equitable',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), Commerce équitable'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_equivalents',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), Produits équivalents'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_externalites',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), Produit prenant en compte les coûts imputés aux externalités environnementales pendant son cycle de vie'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_fermier',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), Fermier'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_france',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), Provenance France'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_hve',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), Haute valeur environnementale'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_label_rouge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), Label rouge'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_local',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), Produit local'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_peche_durable',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), Pêche durable'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_performance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), Produits acquis sur la base de leurs performances en matière environnementale'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_rup',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), Région ultrapériphérique'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='produits_laitiers_short_distribution',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='BOF (Produits laitiers, beurre et œufs), Circuit-court'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_aocaop_igp_stg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, AOC / AOP / IGP / STG'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_bio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, Bio'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_commerce_equitable',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, Commerce équitable'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_equivalents',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, Produits équivalents'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_externalites',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, Produit prenant en compte les coûts imputés aux externalités environnementales pendant son cycle de vie'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_fermier',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, Fermier'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_france',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, Provenance France'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_hve',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, Haute valeur environnementale'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_label_rouge',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, Label rouge'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_local',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, Produit local'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_peche_durable',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, Pêche durable'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_performance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, Produits acquis sur la base de leurs performances en matière environnementale'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_rup',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, Région ultrapériphérique'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='viandes_volailles_short_distribution',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Viandes et volailles fraîches et surgelées, Circuit-court'),
        ),
    ]
