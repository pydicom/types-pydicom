import re
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
PYDICOM_IMPLEMENTATION_UID: UID
RE_VALID_UID: re.Pattern[str]
RE_VALID_UID_PREFIX: re.Pattern[str]
ImplicitVRLittleEndian: UID
ExplicitVRLittleEndian: UID
DeflatedExplicitVRLittleEndian: UID
ExplicitVRBigEndian: UID
JPEGBaseline8Bit: UID
JPEGExtended12Bit: UID
JPEGLossless: UID
JPEGLosslessSV1: UID
JPEGLSLossless: UID
JPEGLSNearLossless: UID
JPEG2000Lossless: UID
JPEG2000: UID
JPEG2000MCLossless: UID
JPEG2000MC: UID
MPEG2MPML: UID
MPEG2MPMLF: UID
MPEG2MPHL: UID
MPEG2MPHLF: UID
MPEG4HP41: UID
MPEG4HP41F: UID
MPEG4HP41BD: UID
MPEG4HP41BDF: UID
MPEG4HP422D: UID
MPEG4HP422DF: UID
MPEG4HP423D: UID
MPEG4HP423DF: UID
MPEG4HP42STEREO: UID
MPEG4HP42STEREOF: UID
HEVCMP51: UID
HEVCM10P51: UID
HTJ2KLossless: UID
HTJ2KLosslessRPCL: UID
HTJ2K: UID
JPIPHTJ2KReferenced: UID
JPIPHTJ2KReferencedDeflate: UID
RLELossless: UID
SMPTEST211020UncompressedProgressiveActiveVideo: UID
SMPTEST211020UncompressedInterlacedActiveVideo: UID
SMPTEST211030PCMDigitalAudio: UID
AllTransferSyntaxes: list[UID]
JPEGTransferSyntaxes: list[UID]
JPEGLSTransferSyntaxes: list[UID]
JPEG2000TransferSyntaxes: list[UID]
MPEGTransferSyntaxes: list[UID]
RLETransferSyntaxes: list[UID]
UncompressedTransferSyntaxes: list[UID]
PrivateTransferSyntaxes: list[UID]

def register_transfer_syntax(uid: str | UID, implicit_vr: bool | None = None, little_endian: bool | None = None) -> UID: ...
def generate_uid(prefix: str | None = ..., entropy_srcs: list[str] | None = None) -> UID: ...

MediaStorageDirectoryStorage: UID
ComputedRadiographyImageStorage: UID
DigitalXRayImageStorageForPresentation: UID
DigitalXRayImageStorageForProcessing: UID
DigitalMammographyXRayImageStorageForPresentation: UID
DigitalMammographyXRayImageStorageForProcessing: UID
DigitalIntraOralXRayImageStorageForPresentation: UID
DigitalIntraOralXRayImageStorageForProcessing: UID
EncapsulatedPDFStorage: UID
EncapsulatedCDAStorage: UID
EncapsulatedSTLStorage: UID
EncapsulatedOBJStorage: UID
EncapsulatedMTLStorage: UID
GrayscaleSoftcopyPresentationStateStorage: UID
SegmentedVolumeRenderingVolumetricPresentationStateStorage: UID
MultipleVolumeRenderingVolumetricPresentationStateStorage: UID
VariableModalityLUTSoftcopyPresentationStateStorage: UID
ColorSoftcopyPresentationStateStorage: UID
PseudoColorSoftcopyPresentationStateStorage: UID
BlendingSoftcopyPresentationStateStorage: UID
XAXRFGrayscaleSoftcopyPresentationStateStorage: UID
GrayscalePlanarMPRVolumetricPresentationStateStorage: UID
CompositingPlanarMPRVolumetricPresentationStateStorage: UID
AdvancedBlendingPresentationStateStorage: UID
VolumeRenderingVolumetricPresentationStateStorage: UID
XRayAngiographicImageStorage: UID
EnhancedXAImageStorage: UID
XRayRadiofluoroscopicImageStorage: UID
EnhancedXRFImageStorage: UID
PositronEmissionTomographyImageStorage: UID
LegacyConvertedEnhancedPETImageStorage: UID
XRay3DAngiographicImageStorage: UID
XRay3DCraniofacialImageStorage: UID
BreastTomosynthesisImageStorage: UID
BreastProjectionXRayImageStorageForPresentation: UID
BreastProjectionXRayImageStorageForProcessing: UID
EnhancedPETImageStorage: UID
BasicStructuredDisplayStorage: UID
IntravascularOpticalCoherenceTomographyImageStorageForPresentation: UID
IntravascularOpticalCoherenceTomographyImageStorageForProcessing: UID
CTImageStorage: UID
EnhancedCTImageStorage: UID
LegacyConvertedEnhancedCTImageStorage: UID
NuclearMedicineImageStorage: UID
CTDefinedProcedureProtocolStorage: UID
CTPerformedProcedureProtocolStorage: UID
ProtocolApprovalStorage: UID
XADefinedProcedureProtocolStorage: UID
XAPerformedProcedureProtocolStorage: UID
InventoryStorage: UID
UltrasoundMultiFrameImageStorage: UID
ParametricMapStorage: UID
MRImageStorage: UID
EnhancedMRImageStorage: UID
MRSpectroscopyStorage: UID
EnhancedMRColorImageStorage: UID
LegacyConvertedEnhancedMRImageStorage: UID
RTImageStorage: UID
RTPhysicianIntentStorage: UID
RTSegmentAnnotationStorage: UID
RTRadiationSetStorage: UID
CArmPhotonElectronRadiationStorage: UID
TomotherapeuticRadiationStorage: UID
RoboticArmRadiationStorage: UID
RTRadiationRecordSetStorage: UID
RTRadiationSalvageRecordStorage: UID
TomotherapeuticRadiationRecordStorage: UID
CArmPhotonElectronRadiationRecordStorage: UID
RTDoseStorage: UID
RoboticRadiationRecordStorage: UID
RTRadiationSetDeliveryInstructionStorage: UID
RTTreatmentPreparationStorage: UID
EnhancedRTImageStorage: UID
EnhancedContinuousRTImageStorage: UID
RTPatientPositionAcquisitionInstructionStorage: UID
RTStructureSetStorage: UID
RTBeamsTreatmentRecordStorage: UID
RTPlanStorage: UID
RTBrachyTreatmentRecordStorage: UID
RTTreatmentSummaryRecordStorage: UID
RTIonPlanStorage: UID
RTIonBeamsTreatmentRecordStorage: UID
DICOSCTImageStorage: UID
DICOSDigitalXRayImageStorageForPresentation: UID
DICOSDigitalXRayImageStorageForProcessing: UID
DICOSThreatDetectionReportStorage: UID
DICOS2DAITStorage: UID
DICOS3DAITStorage: UID
DICOSQuadrupoleResonanceStorage: UID
UltrasoundImageStorage: UID
EnhancedUSVolumeStorage: UID
PhotoacousticImageStorage: UID
EddyCurrentImageStorage: UID
EddyCurrentMultiFrameImageStorage: UID
RawDataStorage: UID
SpatialRegistrationStorage: UID
SpatialFiducialsStorage: UID
DeformableSpatialRegistrationStorage: UID
SegmentationStorage: UID
SurfaceSegmentationStorage: UID
TractographyResultsStorage: UID
RealWorldValueMappingStorage: UID
SurfaceScanMeshStorage: UID
SurfaceScanPointCloudStorage: UID
SecondaryCaptureImageStorage: UID
MultiFrameSingleBitSecondaryCaptureImageStorage: UID
MultiFrameGrayscaleByteSecondaryCaptureImageStorage: UID
MultiFrameGrayscaleWordSecondaryCaptureImageStorage: UID
MultiFrameTrueColorSecondaryCaptureImageStorage: UID
VLEndoscopicImageStorage: UID
VideoEndoscopicImageStorage: UID
VLMicroscopicImageStorage: UID
VideoMicroscopicImageStorage: UID
VLSlideCoordinatesMicroscopicImageStorage: UID
VLPhotographicImageStorage: UID
VideoPhotographicImageStorage: UID
OphthalmicPhotography8BitImageStorage: UID
OphthalmicPhotography16BitImageStorage: UID
StereometricRelationshipStorage: UID
OphthalmicTomographyImageStorage: UID
WideFieldOphthalmicPhotographyStereographicProjectionImageStorage: UID
WideFieldOphthalmicPhotography3DCoordinatesImageStorage: UID
OphthalmicOpticalCoherenceTomographyEnFaceImageStorage: UID
OphthalmicOpticalCoherenceTomographyBscanVolumeAnalysisStorage: UID
VLWholeSlideMicroscopyImageStorage: UID
DermoscopicPhotographyImageStorage: UID
ConfocalMicroscopyImageStorage: UID
ConfocalMicroscopyTiledPyramidalImageStorage: UID
LensometryMeasurementsStorage: UID
AutorefractionMeasurementsStorage: UID
KeratometryMeasurementsStorage: UID
SubjectiveRefractionMeasurementsStorage: UID
VisualAcuityMeasurementsStorage: UID
SpectaclePrescriptionReportStorage: UID
OphthalmicAxialMeasurementsStorage: UID
IntraocularLensCalculationsStorage: UID
MacularGridThicknessAndVolumeReportStorage: UID
OphthalmicVisualFieldStaticPerimetryMeasurementsStorage: UID
OphthalmicThicknessMapStorage: UID
CornealTopographyMapStorage: UID
BasicTextSRStorage: UID
EnhancedSRStorage: UID
ComprehensiveSRStorage: UID
Comprehensive3DSRStorage: UID
ExtensibleSRStorage: UID
ProcedureLogStorage: UID
MammographyCADSRStorage: UID
KeyObjectSelectionDocumentStorage: UID
ChestCADSRStorage: UID
XRayRadiationDoseSRStorage: UID
RadiopharmaceuticalRadiationDoseSRStorage: UID
ColonCADSRStorage: UID
ImplantationPlanSRStorage: UID
AcquisitionContextSRStorage: UID
SimplifiedAdultEchoSRStorage: UID
PatientRadiationDoseSRStorage: UID
PlannedImagingAgentAdministrationSRStorage: UID
PerformedImagingAgentAdministrationSRStorage: UID
EnhancedXRayRadiationDoseSRStorage: UID
WaveformAnnotationSRStorage: UID
TwelveLeadECGWaveformStorage: UID
GeneralECGWaveformStorage: UID
AmbulatoryECGWaveformStorage: UID
General32bitECGWaveformStorage: UID
HemodynamicWaveformStorage: UID
CardiacElectrophysiologyWaveformStorage: UID
BasicVoiceAudioWaveformStorage: UID
GeneralAudioWaveformStorage: UID
ArterialPulseWaveformStorage: UID
RespiratoryWaveformStorage: UID
MultichannelRespiratoryWaveformStorage: UID
RoutineScalpElectroencephalogramWaveformStorage: UID
ElectromyogramWaveformStorage: UID
ElectrooculogramWaveformStorage: UID
SleepElectroencephalogramWaveformStorage: UID
BodyPositionWaveformStorage: UID
ContentAssessmentResultsStorage: UID
MicroscopyBulkSimpleAnnotationsStorage: UID
RTBrachyApplicationSetupDeliveryInstructionStorage: UID
RTBeamsDeliveryInstructionStorage: UID
HangingProtocolStorage: UID
ColorPaletteStorage: UID
GenericImplantTemplateStorage: UID
ImplantAssemblyTemplateStorage: UID
ImplantTemplateGroupStorage: UID
