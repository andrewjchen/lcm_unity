/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

using System;
using System.Collections.Generic;
using System.IO;
using LCM.LCM;
 
namespace forseti2
{
    public sealed class header : LCM.LCM.LCMEncodable
    {
        public int seq;
        public double time;
 
        public header()
        {
        }
 
        public static readonly ulong LCM_FINGERPRINT;
        public static readonly ulong LCM_FINGERPRINT_BASE = 0xa4eee1da213128d1L;
 
        static header()
        {
            LCM_FINGERPRINT = _hashRecursive(new List<String>());
        }
 
        public static ulong _hashRecursive(List<String> classes)
        {
            if (classes.Contains("forseti2.header"))
                return 0L;
 
            classes.Add("forseti2.header");
            ulong hash = LCM_FINGERPRINT_BASE
                ;
            classes.RemoveAt(classes.Count - 1);
            return (hash<<1) + ((hash>>63)&1);
        }
 
        public void Encode(LCMDataOutputStream outs)
        {
            outs.Write((long) LCM_FINGERPRINT);
            _encodeRecursive(outs);
        }
 
        public void _encodeRecursive(LCMDataOutputStream outs)
        {
            outs.Write(this.seq); 
 
            outs.Write(this.time); 
 
        }
 
        public header(byte[] data) : this(new LCMDataInputStream(data))
        {
        }
 
        public header(LCMDataInputStream ins)
        {
            if ((ulong) ins.ReadInt64() != LCM_FINGERPRINT)
                throw new System.IO.IOException("LCM Decode error: bad fingerprint");
 
            _decodeRecursive(ins);
        }
 
        public static forseti2.header _decodeRecursiveFactory(LCMDataInputStream ins)
        {
            forseti2.header o = new forseti2.header();
            o._decodeRecursive(ins);
            return o;
        }
 
        public void _decodeRecursive(LCMDataInputStream ins)
        {
            this.seq = ins.ReadInt32();
 
            this.time = ins.ReadDouble();
 
        }
 
        public forseti2.header Copy()
        {
            forseti2.header outobj = new forseti2.header();
            outobj.seq = this.seq;
 
            outobj.time = this.time;
 
            return outobj;
        }
    }
}
