from rest_framework import routers

from common.views import CostUnitsViewSet
from request.views import RequestViewSet
from library_sample_shared.views import (
    OrganismViewSet,
    IndexTypeViewSet,
    LibraryProtocolViewSet,
    IndexViewSet,
    LibraryTypeViewSet,
    ReadLengthViewSet,
    ConcentrationMethodViewSet,
    LibraryProtocolInvoicingViewSet
)
from library.views import LibrarySampleTree, LibraryViewSet
from sample.views import NucleicAcidTypeViewSet, SampleViewSet
from incoming_libraries.views import IncomingLibrariesViewSet
from index_generator.views import PoolSizeViewSet, IndexGeneratorViewSet,GeneratorIndexTypeViewSet
from library_preparation.views import LibraryPreparationViewSet
from pooling.views import PoolingViewSet
from flowcell.views import (
    SequencerViewSet,
    PoolViewSet,
    FlowcellViewSet,
    FlowcellAnalysisViewSet,
)
from invoicing.views import (
    InvoicingViewSet,
    FixedCostsViewSet,
    LibraryPreparationCostsViewSet,
    SequencingCostsViewSet,
)

from stats.views import RunStatisticsViewSet, SequencesStatisticsViewSet
from metadata_exporter.views import MetadataExporterViewSet


router = routers.DefaultRouter()

router.register(r'requests', RequestViewSet, base_name='request')
router.register(r'cost_units', CostUnitsViewSet, base_name='cost-units')
router.register(r'organisms', OrganismViewSet, base_name='organism')
router.register(r'read_lengths', ReadLengthViewSet, base_name='read-length')
router.register(r'concentration_methods', ConcentrationMethodViewSet, base_name='concentration-method')
router.register(r'index_types', IndexTypeViewSet, base_name='index-type')
router.register(r'generator_index_types', GeneratorIndexTypeViewSet, base_name='generator-index-type')
router.register(r'indices', IndexViewSet, base_name='index')
router.register(r'library_protocols', LibraryProtocolViewSet, base_name='library-protocol')
router.register(r'library_protocols_invoicing', LibraryProtocolInvoicingViewSet, base_name='library-protocol-invoicing')
router.register(r'library_types', LibraryTypeViewSet, base_name='library-type')
router.register(r'nucleic_acid_types', NucleicAcidTypeViewSet, base_name='nucleic-acid-type')
router.register(r'pool_sizes', PoolSizeViewSet, base_name='pool-size')

router.register(r'libraries_and_samples', LibrarySampleTree, base_name='libraries-and-samples')
router.register(r'libraries', LibraryViewSet, base_name='libraries')
router.register(r'samples', SampleViewSet, base_name='samples')

router.register(r'incoming_libraries', IncomingLibrariesViewSet, base_name='incoming-libraries')

router.register(r'index_generator', IndexGeneratorViewSet, base_name='index-generator')

router.register(r'library_preparation', LibraryPreparationViewSet, base_name='library-preparation')

router.register(r'pooling', PoolingViewSet, base_name='pooling')

router.register(r'sequencers', SequencerViewSet, base_name='sequencers')
router.register(r'flowcells', FlowcellViewSet, base_name='flowcells')
router.register(r'pools', PoolViewSet, base_name='pools')

router.register(r'invoicing', InvoicingViewSet, base_name='invoicing')
router.register(r'fixed_costs', FixedCostsViewSet, base_name='fixed-costs')
router.register(r'library_preparation_costs', LibraryPreparationCostsViewSet, base_name='library-preparation-costs')
router.register(r'sequencing_costs', SequencingCostsViewSet, base_name='sequencing-costs')

router.register(r'run_statistics', RunStatisticsViewSet, base_name='run-statistics')
router.register(r'sequences_statistics', SequencesStatisticsViewSet, base_name='sequences-statistics')
router.register(r'analysis_list', FlowcellAnalysisViewSet, base_name='analysis_list')

router.register(r'metadata_exporter', MetadataExporterViewSet, base_name='metadata_exporter')
