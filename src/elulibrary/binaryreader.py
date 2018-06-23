#!/usr/bin/env python3
# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=W0703

"""
This module contains a BinaryReader class that can be used to read binary Data from file.
"""


import datetime
import struct


# @todo fix logging
class BinaryReader:
    """
    Binary reader class that can be used to read binary data from a file.
    """

    def __init__(self,
                 FilePath,
                 Mode='rb',
                 Debug=False,
                 Log=False,
                 LogFileName=r'E:\Raiderz elu project\final_logs\logfile.txt'):
        self.FileStream = open(FilePath, Mode)
        self.Endian = '<'

        # Debugging and Logging
        self.Debug = Debug
        self.Log = Log
        self.LogFileName = LogFileName
        if self.Log:
            self.StartLogging(self.LogFileName)
        else:
            self.LogStream = None

    def AddLog(self, LogMessage):
        try:
            message = '[' + self.CurrentTime() + ']: ' + LogMessage + '\n'
            self.LogStream.write(message)
        except ValueError:
            print("I/O on {0} has closed".format(self.LogStream.name))
            print("Terminating!!")
            exit()
        except AttributeError:
            print("Error while logging! Terminating!!")
            exit()

    def CloseFileStream(self):
        self.FileStream.close()
        if self.Log:
            self.LogStream.close()
            self.Log = False

    def CurrentTime(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def ReadInt(self, NumOfInts):
        Offset = self.FileStream.tell()
        Data = struct.unpack(self.Endian + NumOfInts * 'i',
                             self.FileStream.read(NumOfInts * 4))

        LogInfo = "int: '" + str(Data) + "' at Offset: '" +\
                   str(Offset) + "'."
        if self.Debug:
            print(LogInfo)
        if self.Log:
            self.AddLog(LogInfo)
        return Data

    def ReadUInt(self, NumOfUInts):
        Offset = self.FileStream.tell()
        Data = struct.unpack(self.Endian + NumOfUInts * 'I',
                             self.FileStream.read(NumOfUInts * 4))

        LogInfo = "unsigned int: '" + str(Data) + "' at Offset: '" +\
                   str(Offset) + "'."
        if self.Debug:
            print(LogInfo)
        if self.Log:
            self.AddLog(LogInfo)
        return Data

    def ReadShort(self, NumOfShorts):
        Offset = self.FileStream.tell()
        Data = struct.unpack(self.Endian + NumOfShorts * 'h',
                             self.FileStream.read(NumOfShorts * 2))
        LogInfo = "UShort: '" + str(Data) + "' at Offset: '" +\
                   str(Offset) + "'."
        if self.Debug:
            print(LogInfo)
        if self.Log:
            self.AddLog(LogInfo)
        return Data

    def ReadUShort(self, NumOfUShorts):
        Offset = self.FileStream.tell()
        Data = struct.unpack(self.Endian + NumOfUShorts * 'H',
                             self.FileStream.read(NumOfUShorts * 2))
        LogInfo = "UShort: '" + str(Data) + "' at Offset: '" +\
                   str(Offset) + "'."
        if self.Debug:
            print(LogInfo)
        if self.Log:
            self.AddLog(LogInfo)
        return Data

    def ReadFloat(self, NumOfFloats):
        Offset = self.FileStream.tell()
        Data = struct.unpack(self.Endian + NumOfFloats * 'f',
                             self.FileStream.read(NumOfFloats * 4))
        LogInfo = "float: '" + str(Data) + "' at Offset: '" +\
                   str(Offset) + "'."
        if self.Debug:
            print(LogInfo)
        if self.Log:
            self.AddLog(LogInfo)
        return Data

    def ReadWord(self, Length):
        if Length < 10000:
            Offset = self.FileStream.tell()
            word = ''
            for i in range(Length):
                # For some reason char will be b''
                char = struct.unpack('c',
                                     self.FileStream.read(1))[0]
                if ord(char) != 0:
                    word += char.decode('ascii')
            LogInfo = "word: '" + word + "' at Offset: '" +\
                       str(Offset) + "'."
            if self.Debug:
                print(LogInfo)
            if self.Log:
                self.AddLog(LogInfo)
            return word
        else:
            print("Too Long. Quitting!!")
            quit()

    def Seek(self, Offset, Whence=0):
        self.FileStream.seek(Offset, Whence)

    def StartLogging(self, LogFileName):
        self.LogStream = open(LogFileName, 'w')

    def Tell(self):
        Offset = self.FileStream.tell()
        if self.Debug:
            print("Current Offset is: ", Offset)
        return Offset


"""
Functions to read binary data directly by passing the filestream object
"""
def ReadInt(FileStream, NumOfInts, Offset=None, Endian='<'):
    """
    Reads integers from filestream and returns them in a tuple\n
    Little endian by default\n
    @param NumOfInts Number of integers to read\n
    @param Offset Cursor offset to read binary data in FileStream from. default=None.\n
    @return Returns the tuple of integers\n
    """
    if Offset != None:
        FileStream.seek(Offset)
    else:
        pass

    # If an exception occurs while unpacking, it should be handled in upper level function
    Data = struct.unpack(Endian + NumOfInts * 'i', FileStream.read(NumOfInts * 4))
    return Data


def ReadUInt(FileStream, NumOfUInts, Offset=None, Endian='<'):
    """
    Reads unsigned integers from filestream and returns them in a tuple\n
    Little Endian by default\n
    @param NumOfUInts Number of unsigned integers to read\n
    @param Offset Cursor offset to read binary data in FileStream from. default=None.\n
    @return Returns the tuple of unsigned integers\n
    """
    if Offset != None:
        FileStream.seek(Offset)
    else:
        pass

    # If an exception occurs while unpacking, it should be handled in upper level function
    Data = struct.unpack(Endian + NumOfUInts * 'I', FileStream.read(NumOfUInts * 4))
    return Data


def ReadWord(FileStream, Offset=None, Endian='<'):
    """
    Reads a string from filestream. This function assumes that the first\n
    first 4 bytes in FileStream represent an integer.\n
    This integer is used to determine the size of string to be read.\n
    Assumes characters to be ascii\n

    @param Offset Cursor offset to read binary data in FileStream from. default=None.\n
    @return Returns the string read\n
    """
    if Offset != None:
        FileStream.seek(Offset)
    else:
        pass

    StringSize = ReadInt(FileStream, 1, Offset, Endian)[0]
    Word = ''
    for i in range(StringSize):
        # If an exception occurs while unpacking, it should be handled in upper level function
        # Character read will be b''
        Char = struct.unpack('c', FileStream.read(1))[0]
        if ord(Char) != 0:
            Word += Char.decode('ascii')
    return Word


def ReadShort(FileStream, NumOfShorts, Offset=None, Endian='<'):
    """
    Reads short integers from filestream and returns them in a tuple\n
    Little endian by default\n
    @param NumOfShorts Number of short integers to read\n
    @param Offset Cursor offset to read binary data in FileStream from. default=None.\n
    @return Returns the tuple of short integers\n
    """
    if Offset != None:
        FileStream.seek(Offset)
    else:
        pass

    # If an exception occurs while unpacking, it should be handled in upper level function
    Data = struct.unpack(Endian + NumOfShorts * 'h', FileStream.read(NumOfShorts * 2))
    return Data
    

def ReadUShort(FileStream, NumOfUShorts, Offset=None, Endian='<'):
    """
    Reads unsigned short integers from filestream and returns them in a tuple\n
    Little endian by default\n
    @param NumOfUShorts Number of unsigned short integers to read\n
    @param Offset Cursor offset to read binary data in FileStream from. default=None.\n
    @return Returns the tuple of unsigned short integers\n
    """
    if Offset != None:
        FileStream.seek(Offset)
    else:
        pass

    # If an exception occurs while unpacking, it should be handled in upper level function
    Data = struct.unpack(Endian + NumOfUShorts * 'H', FileStream.read(NumOfUShorts * 2))
    return Data


def ReadFloat(FileStream, NumOfFloats, Offset=None, Endian='<'):
    """
    Reads floats from filestream and returns them in a tuple\n
    Little endian by default\n
    @param NumOfFloats Number of floats to read\n
    @param Offset Cursor offset to read binary data in FileStream from. default=None.\n
    @return Returns the tuple of floats\n
    """
    if Offset != None:
        FileStream.seek(Offset)
    else:
        pass

    # If an exception occurs while unpacking, it should be handled in upper level function
    Data = struct.unpack(Endian + NumOfFloats * 'f', FileStream.read(NumOfFloats * 4))
    return Data
