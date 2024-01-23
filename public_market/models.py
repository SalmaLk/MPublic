from django.db import models

# Create your models here.
from django.db import models

class Autorite(models.Model):
    id_autorite = models.AutoField(primary_key=True)
    nom_autorite = models.CharField(max_length=255)
    adresse_autorite = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'autorite'
   

class Contrat(models.Model):
    id_contrat = models.AutoField(primary_key=True)
    id_four = models.ForeignKey('Fournisseur', on_delete=models.CASCADE, db_column='id_four')
    id_marche = models.ForeignKey('Marche', on_delete=models.CASCADE, db_column='id_marche')
    duree = models.IntegerField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'contrat'


class Fournisseur(models.Model):
    id_four = models.AutoField(primary_key=True)
    nom_four = models.CharField(max_length=255)
    adresse_four = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'fournisseur'


class Marche(models.Model):
    id_marche = models.AutoField(primary_key=True)
    id_ppm = models.ForeignKey('Ppm', on_delete=models.CASCADE, db_column='id_ppm')
    ppm = models.CharField(max_length=10, blank=True, null=True,  
                           choices=[
                               ('PPM-2019', 'PPM-2019'), 
                               ('PPM-2020', 'PPM-2020'), 
                               ('PPM2021', 'PPM2021'),
                               ('PPM2022', 'PPM2022')])
    inscription_ppm =models.BooleanField(null=True)
    ac = models.CharField(max_length=255, blank=True, null=True)
    ref_activite = models.CharField(max_length=255, blank=True, null=True)
    type_activite = models.CharField(max_length=255, blank=True,  
                                      choices=[
                                          ('T', ' Travaux'), 
                                          ('F', ' Fournitures'), 
                                          ('S', ' Services'), 
                                          ('PI', ' Prestations Intellectuelles')])
    mode = models.CharField(max_length=255, blank=True, null=True, 
                            choices=[
                                 ('SQC', 'Sélection sur la Qualité du Consultant'),
                                 ('SBQC', 'Sélection sur la Base de qualité et Cout'),
                                 ('SBD', 'Sélection sur la Base de Document'),
                                 ('SMC', 'Sélection du Moindre Cout'),
                                 ('AON', 'Appel d\'Offre National'),
                                 ('AOI', 'Appel d\'Offre International'),
                                 ('AOR', 'Appel d\'Offre national Restreint'),
                                 ('AORI', 'Appel d\'Offre Restreint International'),
                                 ('ED', 'En Mode Direct')])
    date_prev_lancement_activite = models.DateField(blank=True, null=True)
    date_prev_de_reception = models.DateField(blank=True, null=True)
    budget_prev = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    devise = models.CharField(max_length=3, 
                               choices=[
                                   ('MRU', 'MRU'), 
                                   ('USD', 'USD'), 
                                   ('EUR', 'EUR')])
    source_de_financement = models.CharField(max_length=100, 
                                              choices=[
                                                  ('B.E', 'Budget de l\'Etat'), 
                                                  ('B.F', 'Bayeur de Fond ou Budget Externe'), 
                                                  ('B.E/B.F', 'Projet financé en deux Partie Etat et B.F')])
    lib_source_de_financement = models.CharField(max_length=255, blank=True, null=True)
    date_publication_activite = models.DateField(blank=True, null=True)
    niveau_suivi = models.CharField(max_length=255, null=True, 
                                    choices=[
                                        ('AC', 'Autorité Contractante'),
                                        ('CPMP', 'Commission de Passation des Marchés Publics'),
                                        ('CNCMP', 'Commission Nationale de Contrôle des Marchés Publics'), 
                                        ('ARMP', 'Autorité de Régulation des Marchés Publics'),
                                        ('ANO-B.F', 'Avis de Non Objection du Bayeur de Fond')])
    etape = models.CharField(max_length=255, null=True,
                                     choices=[
                                             ('AMI','Avis de Manifestation d\'Intérêt'),
                                             ('DP', 'Demande de Proposition'),
                                             ('ET', 'Etude Technique'),
                                             ('EF', 'Etude Financière'), 
                                             ('PM', 'Projet de Marché'),
                                             ('Marché', 'Marché attribué'),
                                             ('DAO', 'Dossier d\'Appel d\'Offre'),
                                             ('PE', 'Phase d\'Evaluation')])
    approbation = models.CharField(max_length=255, blank=True, null=True,
                                  choices=[
                                            ('NA', 'Non approuvé'), 
                                            ('Reporté', 'Reporté'), 
                                            ('ASR', 'Approuvé sous réserve'), 
                                            ('Approuvé', 'Approuvé'), 
                                            ('MA', 'Marché attribué')])
    date_attribution = models.DateField(blank=True, null=True)
    attributaire = models.CharField(max_length=255, blank=True, null=True)
    montant_total_du_marche = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_signature_ac = models.DateField(blank=True, null=True)
    num_marche = models.CharField(max_length=255, blank=True, null=True)
    date_numerotation = models.DateField(blank=True, null=True)
    date_notification = models.DateField(blank=True, null=True)
    delai_execution_en_jour = models.IntegerField(blank=True, null=True)
    date_de_reception = models.DateField(blank=True, null=True)
    retard_constate_en_jour = models.IntegerField(blank=True, null=True)
    etat_du_marche = models.CharField(max_length=255, blank=True, null=True,
                                       choices=[
                                           ('PA', 'Projet Marché'), 
                                           ('MECE', 'Marché En cours d\'Exécution'), 
                                           ('MER', 'Marché En Retard'),
                                           ('AAN', 'Activité Annulée'), 
                                           ('MR', 'Marché Resilié'), 
                                           ('MREC', 'Marché Réceptionné')])
    observation = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'marche'


class Piecedetachee(models.Model):
    id_piece = models.AutoField(primary_key=True)
    id_marche = models.ForeignKey(Marche, on_delete=models.CASCADE, db_column='id_marche')
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    fichier =  models.FileField(upload_to='documents/')
    date_ajout = models.DateTimeField()

    class Meta:
        db_table = 'piecedetachee'


class Ppm(models.Model):
    id_ppm = models.AutoField(primary_key=True)
    annee_ppm = models.IntegerField()
    id_autorite = models.ForeignKey(Autorite, on_delete=models.CASCADE, db_column='id_autorite')

    class Meta:
        db_table = 'ppm'


class Soumission(models.Model):
    id_soum = models.AutoField(primary_key=True)
    date_soumission = models.DateField(blank=True, null=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_four = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, db_column='id_four')
    id_marche = models.ForeignKey(Marche, on_delete=models.CASCADE, db_column='id_marche')

    class Meta:
        db_table = 'soumission'
