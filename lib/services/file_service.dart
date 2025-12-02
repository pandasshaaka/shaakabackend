import 'dart:io';
import 'dart:convert';
import 'package:http/http.dart' as http;

class FileService {
  final String baseUrl;
  FileService({required this.baseUrl});

  Future<String?> uploadImage(File file) async {
    final uri = Uri.parse('$baseUrl/files/upload');
    final req = http.MultipartRequest('POST', uri);
    req.files.add(await http.MultipartFile.fromPath('file', file.path));
    final res = await req.send();
    if (res.statusCode != 200) return null;
    final body = await res.stream.bytesToString();
    final map = jsonDecode(body) as Map<String, dynamic>;
    final url = map['url'] as String?;
    if (url == null) return null;
    return '$baseUrl$url';
  }
}
