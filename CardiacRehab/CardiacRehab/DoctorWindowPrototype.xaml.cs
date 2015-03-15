using Coding4Fun.Kinect.KinectService.Common;
using Coding4Fun.Kinect.KinectService.Listeners;
using Coding4Fun.Kinect.KinectService.WpfClient;
using DynamicDataDisplaySample.ECGViewModel;
using Microsoft.Research.DynamicDataDisplay;
using Microsoft.Research.DynamicDataDisplay.DataSources;
using Microsoft.Kinect;
using Microsoft.Kinect.Toolkit;
using NAudio.Wave;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.Windows.Threading;
using ColorImageFormat = Microsoft.Kinect.ColorImageFormat;
using ColorImageFrame = Microsoft.Kinect.ColorImageFrame;
using System.Threading;
using System.IO;

namespace CardiacRehab
{
    /// <summary>
    /// Interaction logic for DoctorWindowPrototype.xaml
    /// </summary>
    public partial class DoctorWindowPrototype : Window
    {
        List<ContactInfo> PatientList;

        String wirelessIP;

        // all TCP sockets getting biometric data from the patients
        ClinicianSockets patient1hrox;
        ClinicianSockets patient1uibp;
        ClinicianSockets patient1ecg;
        ClinicianSockets patient1bike;

        //ClinicianSockets patient2hrox;
        //ClinicianSockets patient2uibp;
        //ClinicianSockets patient2ecg;
        //ClinicianSockets patient2bike;

        //ClinicianSockets patient3hrox;
        //ClinicianSockets patient3uibp;
        //ClinicianSockets patient3ecg;
        //ClinicianSockets patient3bike;

        //ClinicianSockets patient4hrox;
        //ClinicianSockets patient4uibp;
        //ClinicianSockets patient4ecg;
        //ClinicianSockets patient4bike;

        //ClinicianSockets patient5hrox;
        //ClinicianSockets patient5uibp;
        //ClinicianSockets patient5ecg;
        //ClinicianSockets patient5bike;

        //ClinicianSockets patient6hrox;
        //ClinicianSockets patient6uibp;
        //ClinicianSockets patient6ecg;
        //ClinicianSockets patient6bike;

        WaveOut wo = new WaveOut();
        WaveFormat wf = new WaveFormat(16000, 1);
        BufferedWaveProvider mybufferwp = null;
        public float oldVolume;

        private FullScreenWindow fullscreenview = null;
        bool[] warningStatus = new bool[6];

        TextWriter _writer;
        public DoctorWindowPrototype()
        {
            InitializeComponent();
        }
    }
}
