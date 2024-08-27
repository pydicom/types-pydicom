from _typeshed import Incomplete
from pydicom import config as config
from pydicom._uid_dict import UID_dictionary as UID_dictionary
from pydicom.config import disable_value_validation as disable_value_validation
from pydicom.valuerep import STR_VR_REGEXES as STR_VR_REGEXES, validate_value as validate_value

class UID(str):
    def __new__(cls, val: str, validation_mode: int | None = None) -> UID: ...
    @property
    def is_implicit_VR(self) -> bool: ...
    @property
    def is_little_endian(self) -> bool: ...
    @property
    def is_transfer_syntax(self) -> bool: ...
    @property
    def is_deflated(self) -> bool: ...
    @property
    def is_encapsulated(self) -> bool: ...
    @property
    def is_compressed(self) -> bool: ...
    @property
    def keyword(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def type(self) -> str: ...
    @property
    def info(self) -> str: ...
    @property
    def is_retired(self) -> bool: ...
    @property
    def is_private(self) -> bool: ...
    @property
    def is_valid(self) -> bool: ...
    def set_private_encoding(self, implicit_vr: bool, little_endian: bool) -> None: ...

PYDICOM_ROOT_UID: str
PYDICOM_IMPLEMENTATION_UID: Incomplete
RE_VALID_UID: Incomplete
RE_VALID_UID_PREFIX: Incomplete
ImplicitVRLittleEndian: Incomplete
ExplicitVRLittleEndian: Incomplete
DeflatedExplicitVRLittleEndian: Incomplete
ExplicitVRBigEndian: Incomplete
JPEGBaseline8Bit: Incomplete
JPEGExtended12Bit: Incomplete
JPEGLossless: Incomplete
JPEGLosslessSV1: Incomplete
JPEGLSLossless: Incomplete
JPEGLSNearLossless: Incomplete
JPEG2000Lossless: Incomplete
JPEG2000: Incomplete
JPEG2000MCLossless: Incomplete
JPEG2000MC: Incomplete
MPEG2MPML: Incomplete
MPEG2MPMLF: Incomplete
MPEG2MPHL: Incomplete
MPEG2MPHLF: Incomplete
MPEG4HP41: Incomplete
MPEG4HP41F: Incomplete
MPEG4HP41BD: Incomplete
MPEG4HP41BDF: Incomplete
MPEG4HP422D: Incomplete
MPEG4HP422DF: Incomplete
MPEG4HP423D: Incomplete
MPEG4HP423DF: Incomplete
MPEG4HP42STEREO: Incomplete
MPEG4HP42STEREOF: Incomplete
HEVCMP51: Incomplete
HEVCM10P51: Incomplete
HTJ2KLossless: Incomplete
HTJ2KLosslessRPCL: Incomplete
HTJ2K: Incomplete
JPIPHTJ2KReferenced: Incomplete
JPIPHTJ2KReferencedDeflate: Incomplete
RLELossless: Incomplete
SMPTEST211020UncompressedProgressiveActiveVideo: Incomplete
SMPTEST211020UncompressedInterlacedActiveVideo: Incomplete
SMPTEST211030PCMDigitalAudio: Incomplete
AllTransferSyntaxes: Incomplete
JPEGTransferSyntaxes: Incomplete
JPEGLSTransferSyntaxes: Incomplete
JPEG2000TransferSyntaxes: Incomplete
MPEGTransferSyntaxes: Incomplete
RLETransferSyntaxes: Incomplete
UncompressedTransferSyntaxes: Incomplete
PrivateTransferSyntaxes: Incomplete

def register_transfer_syntax(uid: str | UID, implicit_vr: bool | None = None, little_endian: bool | None = None) -> UID: ...
def generate_uid(prefix: str | None = ..., entropy_srcs: list[str] | None = None) -> UID: ...

MediaStorageDirectoryStorage: Incomplete
ComputedRadiographyImageStorage: Incomplete
DigitalXRayImageStorageForPresentation: Incomplete
DigitalXRayImageStorageForProcessing: Incomplete
DigitalMammographyXRayImageStorageForPresentation: Incomplete
DigitalMammographyXRayImageStorageForProcessing: Incomplete
DigitalIntraOralXRayImageStorageForPresentation: Incomplete
DigitalIntraOralXRayImageStorageForProcessing: Incomplete
EncapsulatedPDFStorage: Incomplete
EncapsulatedCDAStorage: Incomplete
EncapsulatedSTLStorage: Incomplete
EncapsulatedOBJStorage: Incomplete
EncapsulatedMTLStorage: Incomplete
GrayscaleSoftcopyPresentationStateStorage: Incomplete
SegmentedVolumeRenderingVolumetricPresentationStateStorage: Incomplete
MultipleVolumeRenderingVolumetricPresentationStateStorage: Incomplete
VariableModalityLUTSoftcopyPresentationStateStorage: Incomplete
ColorSoftcopyPresentationStateStorage: Incomplete
PseudoColorSoftcopyPresentationStateStorage: Incomplete
BlendingSoftcopyPresentationStateStorage: Incomplete
XAXRFGrayscaleSoftcopyPresentationStateStorage: Incomplete
GrayscalePlanarMPRVolumetricPresentationStateStorage: Incomplete
CompositingPlanarMPRVolumetricPresentationStateStorage: Incomplete
AdvancedBlendingPresentationStateStorage: Incomplete
VolumeRenderingVolumetricPresentationStateStorage: Incomplete
XRayAngiographicImageStorage: Incomplete
EnhancedXAImageStorage: Incomplete
XRayRadiofluoroscopicImageStorage: Incomplete
EnhancedXRFImageStorage: Incomplete
PositronEmissionTomographyImageStorage: Incomplete
LegacyConvertedEnhancedPETImageStorage: Incomplete
XRay3DAngiographicImageStorage: Incomplete
XRay3DCraniofacialImageStorage: Incomplete
BreastTomosynthesisImageStorage: Incomplete
BreastProjectionXRayImageStorageForPresentation: Incomplete
BreastProjectionXRayImageStorageForProcessing: Incomplete
EnhancedPETImageStorage: Incomplete
BasicStructuredDisplayStorage: Incomplete
IntravascularOpticalCoherenceTomographyImageStorageForPresentation: Incomplete
IntravascularOpticalCoherenceTomographyImageStorageForProcessing: Incomplete
CTImageStorage: Incomplete
EnhancedCTImageStorage: Incomplete
LegacyConvertedEnhancedCTImageStorage: Incomplete
NuclearMedicineImageStorage: Incomplete
CTDefinedProcedureProtocolStorage: Incomplete
CTPerformedProcedureProtocolStorage: Incomplete
ProtocolApprovalStorage: Incomplete
XADefinedProcedureProtocolStorage: Incomplete
XAPerformedProcedureProtocolStorage: Incomplete
InventoryStorage: Incomplete
UltrasoundMultiFrameImageStorage: Incomplete
ParametricMapStorage: Incomplete
MRImageStorage: Incomplete
EnhancedMRImageStorage: Incomplete
MRSpectroscopyStorage: Incomplete
EnhancedMRColorImageStorage: Incomplete
LegacyConvertedEnhancedMRImageStorage: Incomplete
RTImageStorage: Incomplete
RTPhysicianIntentStorage: Incomplete
RTSegmentAnnotationStorage: Incomplete
RTRadiationSetStorage: Incomplete
CArmPhotonElectronRadiationStorage: Incomplete
TomotherapeuticRadiationStorage: Incomplete
RoboticArmRadiationStorage: Incomplete
RTRadiationRecordSetStorage: Incomplete
RTRadiationSalvageRecordStorage: Incomplete
TomotherapeuticRadiationRecordStorage: Incomplete
CArmPhotonElectronRadiationRecordStorage: Incomplete
RTDoseStorage: Incomplete
RoboticRadiationRecordStorage: Incomplete
RTRadiationSetDeliveryInstructionStorage: Incomplete
RTTreatmentPreparationStorage: Incomplete
EnhancedRTImageStorage: Incomplete
EnhancedContinuousRTImageStorage: Incomplete
RTPatientPositionAcquisitionInstructionStorage: Incomplete
RTStructureSetStorage: Incomplete
RTBeamsTreatmentRecordStorage: Incomplete
RTPlanStorage: Incomplete
RTBrachyTreatmentRecordStorage: Incomplete
RTTreatmentSummaryRecordStorage: Incomplete
RTIonPlanStorage: Incomplete
RTIonBeamsTreatmentRecordStorage: Incomplete
DICOSCTImageStorage: Incomplete
DICOSDigitalXRayImageStorageForPresentation: Incomplete
DICOSDigitalXRayImageStorageForProcessing: Incomplete
DICOSThreatDetectionReportStorage: Incomplete
DICOS2DAITStorage: Incomplete
DICOS3DAITStorage: Incomplete
DICOSQuadrupoleResonanceStorage: Incomplete
UltrasoundImageStorage: Incomplete
EnhancedUSVolumeStorage: Incomplete
PhotoacousticImageStorage: Incomplete
EddyCurrentImageStorage: Incomplete
EddyCurrentMultiFrameImageStorage: Incomplete
RawDataStorage: Incomplete
SpatialRegistrationStorage: Incomplete
SpatialFiducialsStorage: Incomplete
DeformableSpatialRegistrationStorage: Incomplete
SegmentationStorage: Incomplete
SurfaceSegmentationStorage: Incomplete
TractographyResultsStorage: Incomplete
RealWorldValueMappingStorage: Incomplete
SurfaceScanMeshStorage: Incomplete
SurfaceScanPointCloudStorage: Incomplete
SecondaryCaptureImageStorage: Incomplete
MultiFrameSingleBitSecondaryCaptureImageStorage: Incomplete
MultiFrameGrayscaleByteSecondaryCaptureImageStorage: Incomplete
MultiFrameGrayscaleWordSecondaryCaptureImageStorage: Incomplete
MultiFrameTrueColorSecondaryCaptureImageStorage: Incomplete
VLEndoscopicImageStorage: Incomplete
VideoEndoscopicImageStorage: Incomplete
VLMicroscopicImageStorage: Incomplete
VideoMicroscopicImageStorage: Incomplete
VLSlideCoordinatesMicroscopicImageStorage: Incomplete
VLPhotographicImageStorage: Incomplete
VideoPhotographicImageStorage: Incomplete
OphthalmicPhotography8BitImageStorage: Incomplete
OphthalmicPhotography16BitImageStorage: Incomplete
StereometricRelationshipStorage: Incomplete
OphthalmicTomographyImageStorage: Incomplete
WideFieldOphthalmicPhotographyStereographicProjectionImageStorage: Incomplete
WideFieldOphthalmicPhotography3DCoordinatesImageStorage: Incomplete
OphthalmicOpticalCoherenceTomographyEnFaceImageStorage: Incomplete
OphthalmicOpticalCoherenceTomographyBscanVolumeAnalysisStorage: Incomplete
VLWholeSlideMicroscopyImageStorage: Incomplete
DermoscopicPhotographyImageStorage: Incomplete
ConfocalMicroscopyImageStorage: Incomplete
ConfocalMicroscopyTiledPyramidalImageStorage: Incomplete
LensometryMeasurementsStorage: Incomplete
AutorefractionMeasurementsStorage: Incomplete
KeratometryMeasurementsStorage: Incomplete
SubjectiveRefractionMeasurementsStorage: Incomplete
VisualAcuityMeasurementsStorage: Incomplete
SpectaclePrescriptionReportStorage: Incomplete
OphthalmicAxialMeasurementsStorage: Incomplete
IntraocularLensCalculationsStorage: Incomplete
MacularGridThicknessAndVolumeReportStorage: Incomplete
OphthalmicVisualFieldStaticPerimetryMeasurementsStorage: Incomplete
OphthalmicThicknessMapStorage: Incomplete
CornealTopographyMapStorage: Incomplete
BasicTextSRStorage: Incomplete
EnhancedSRStorage: Incomplete
ComprehensiveSRStorage: Incomplete
Comprehensive3DSRStorage: Incomplete
ExtensibleSRStorage: Incomplete
ProcedureLogStorage: Incomplete
MammographyCADSRStorage: Incomplete
KeyObjectSelectionDocumentStorage: Incomplete
ChestCADSRStorage: Incomplete
XRayRadiationDoseSRStorage: Incomplete
RadiopharmaceuticalRadiationDoseSRStorage: Incomplete
ColonCADSRStorage: Incomplete
ImplantationPlanSRStorage: Incomplete
AcquisitionContextSRStorage: Incomplete
SimplifiedAdultEchoSRStorage: Incomplete
PatientRadiationDoseSRStorage: Incomplete
PlannedImagingAgentAdministrationSRStorage: Incomplete
PerformedImagingAgentAdministrationSRStorage: Incomplete
EnhancedXRayRadiationDoseSRStorage: Incomplete
WaveformAnnotationSRStorage: Incomplete
TwelveLeadECGWaveformStorage: Incomplete
GeneralECGWaveformStorage: Incomplete
AmbulatoryECGWaveformStorage: Incomplete
General32bitECGWaveformStorage: Incomplete
HemodynamicWaveformStorage: Incomplete
CardiacElectrophysiologyWaveformStorage: Incomplete
BasicVoiceAudioWaveformStorage: Incomplete
GeneralAudioWaveformStorage: Incomplete
ArterialPulseWaveformStorage: Incomplete
RespiratoryWaveformStorage: Incomplete
MultichannelRespiratoryWaveformStorage: Incomplete
RoutineScalpElectroencephalogramWaveformStorage: Incomplete
ElectromyogramWaveformStorage: Incomplete
ElectrooculogramWaveformStorage: Incomplete
SleepElectroencephalogramWaveformStorage: Incomplete
BodyPositionWaveformStorage: Incomplete
ContentAssessmentResultsStorage: Incomplete
MicroscopyBulkSimpleAnnotationsStorage: Incomplete
RTBrachyApplicationSetupDeliveryInstructionStorage: Incomplete
RTBeamsDeliveryInstructionStorage: Incomplete
HangingProtocolStorage: Incomplete
ColorPaletteStorage: Incomplete
GenericImplantTemplateStorage: Incomplete
ImplantAssemblyTemplateStorage: Incomplete
ImplantTemplateGroupStorage: Incomplete
