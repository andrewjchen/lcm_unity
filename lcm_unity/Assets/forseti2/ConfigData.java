/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package forseti2;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class ConfigData implements lcm.lcm.LCMEncodable
{
    public String ConfigFile;
    public int TeamNumber;
 
    public ConfigData()
    {
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0x9c8a3ed3b401713fL;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(forseti2.ConfigData.class))
            return 0L;
 
        classes.add(forseti2.ConfigData.class);
        long hash = LCM_FINGERPRINT_BASE
            ;
        classes.remove(classes.size() - 1);
        return (hash<<1) + ((hash>>63)&1);
    }
 
    public void encode(DataOutput outs) throws IOException
    {
        outs.writeLong(LCM_FINGERPRINT);
        _encodeRecursive(outs);
    }
 
    public void _encodeRecursive(DataOutput outs) throws IOException
    {
        char[] __strbuf = null;
        __strbuf = new char[this.ConfigFile.length()]; this.ConfigFile.getChars(0, this.ConfigFile.length(), __strbuf, 0); outs.writeInt(__strbuf.length+1); for (int _i = 0; _i < __strbuf.length; _i++) outs.write(__strbuf[_i]); outs.writeByte(0); 
 
        outs.writeInt(this.TeamNumber); 
 
    }
 
    public ConfigData(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public ConfigData(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static forseti2.ConfigData _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        forseti2.ConfigData o = new forseti2.ConfigData();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        char[] __strbuf = null;
        __strbuf = new char[ins.readInt()-1]; for (int _i = 0; _i < __strbuf.length; _i++) __strbuf[_i] = (char) (ins.readByte()&0xff); ins.readByte(); this.ConfigFile = new String(__strbuf);
 
        this.TeamNumber = ins.readInt();
 
    }
 
    public forseti2.ConfigData copy()
    {
        forseti2.ConfigData outobj = new forseti2.ConfigData();
        outobj.ConfigFile = this.ConfigFile;
 
        outobj.TeamNumber = this.TeamNumber;
 
        return outobj;
    }
 
}
